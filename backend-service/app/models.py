from config import db, ma

# Job id : int
# Job name : string
# Start date : timestamp
# End date : timestamp
# Goal : string
# Data sources : [string]
# Domain : string
# Full Company name* : string
# Company URL* : string
# Status


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_name = db.Column(db.String(255))
    start_date = db.Column('start_date', db.DateTime, nullable=False)
    end_date = db.Column('end_date', db.DateTime, nullable=False)
    goal = db.Column(db.String(255))
    data_sources = db.Column(db.String(255))
    domain = db.Column(db.String(255))
    company_name = db.Column(db.String(255))
    company_url = db.Column(db.String(255))
    status = db.Column(db.Integer)

    def __repr__(self):
        return '<Job> {}>'.format(self.job_name)


class JobSchema(ma.ModelSchema):
    class Meta:
        model = Job
        sqla_session = db.session
