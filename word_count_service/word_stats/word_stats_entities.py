from word_count_service.db.db_manager import db


class WordStats(db.Model):

    __tablename__ = "word_stats"
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255))
    results = db.relationship('WordStatsResult', backref='word_stats', lazy=False)
    user_id= db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)


class WordStatsResult(db.Model):
    __tablename__ = "word_stats_result"
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(255))
    frequency = db.Column(db.Integer, nullable=False)
    word_stats_id = db.Column(db.Integer, db.ForeignKey('word_stats.id'),
        nullable=False)