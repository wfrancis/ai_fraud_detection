from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tms.db'
db = SQLAlchemy(app)


class Tournament(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    entry_fee = db.Column(db.Float, default=0)
    total_prize_pool = db.Column(db.Float, nullable=False)
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_time = db.Column(db.DateTime, nullable=False)
    payout_structure = db.Column(db.Text, nullable=True)  # Store as string, convert to/from JSON
    status = db.Column(db.String(20), default='Scheduled')
    participant_limit = db.Column(db.Integer, nullable=False)
    current_participants = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'entry_fee': self.entry_fee,
            'total_prize_pool': self.total_prize_pool,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat(),
            'payout_structure': json.loads(self.payout_structure) if self.payout_structure else None,
            'status': self.status,
            'participant_limit': self.participant_limit,
            'current_participants': self.current_participants
        }


class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'), nullable=False)
    score = db.Column(db.Float, default=0)

    tournament = db.relationship('Tournament', backref=db.backref('participants', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'score': self.score
        }


@app.route('/tournament/', methods=['POST'])
def create_tournament():
    data = request.json
    if not all(k in data for k in ['name', 'total_prize_pool', 'end_time', 'participant_limit']):
        return jsonify({"error": "Missing required fields"}), 400

    new_tournament = Tournament(
        name=data['name'],
        entry_fee=data.get('entry_fee', 0),
        total_prize_pool=data['total_prize_pool'],
        end_time=datetime.fromisoformat(data['end_time']),
        payout_structure=json.dumps(data.get('payout_structure')),
        participant_limit=data['participant_limit']
    )
    db.session.add(new_tournament)
    db.session.commit()
    return jsonify(new_tournament.to_dict()), 201


@app.route('/tournament/<int:tournament_id>/register/', methods=['POST'])
def register_for_tournament(tournament_id):
    tournament = Tournament.query.get_or_404(tournament_id)

    if tournament.current_participants >= tournament.participant_limit:
        return jsonify({"error": "Tournament is full"}), 400

    if tournament.status not in ['Scheduled', 'Open']:
        return jsonify({"error": "Registration not available for this tournament"}), 400

    data = request.json
    if not all(k in data for k in ['username', 'email']):
        return jsonify({"error": "Missing required participant information"}), 400

    new_participant = Participant(
        username=data['username'],
        email=data['email'],
        tournament_id=tournament_id
    )
    db.session.add(new_participant)
    tournament.current_participants += 1
    db.session.commit()
    return jsonify({"message": "Registered successfully", "participant": new_participant.to_dict()}), 201


@app.route('/tournament/<int:tournament_id>/score/', methods=['POST'])
def update_score(tournament_id):
    data = request.json
    if 'username' not in data or 'score' not in data:
        return jsonify({"error": "Missing required score update information"}), 400

    participant = Participant.query.filter_by(tournament_id=tournament_id, username=data['username']).first_or_404()
    participant.score = data['score']
    db.session.commit()
    return jsonify({"message": "Score updated successfully", "participant": participant.to_dict()}), 200


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)