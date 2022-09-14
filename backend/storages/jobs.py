import logging
from datetime import date

from sqlalchemy.exc import IntegrityError

from backend.database.db import db_session
from backend.database.models import Job
from backend.errors import ConflictError, NotFoundError
from backend.schemas.job import CorrectJob

logger = logging.getLogger(__name__)


class JobsStorage():
    name = 'jobs'

    def add(self, job: CorrectJob):
        today = date.today()
        new_job = Job(
            company_uid=job.company_uid,
            name=job.name,
            salary=job.salary,
            description=job.description,
            date_published=job.date_published,
            date_expiring=job.date_expiring,
            url=job.url,
            date_added=today,
        )

        db_session.add(new_job)
        try:
            db_session.commit()
        except IntegrityError as err:
            logger.warning(err)
            raise ConflictError(
                self.name,
                f'company_uid: {job.company_uid} does not exist',
            ) from err

        return CorrectJob.from_orm(new_job)

    def delete(self, uid):
        job = Job.query.filter(Job.uid == uid).first()
        if not job:
            raise NotFoundError(self.name, f'uid {uid} not found')

        db_session.delete(job)
        db_session.commit()

    def update(self, job: CorrectJob):
        changed_job = Job.query.filter(Job.uid == job.uid).first()
        if not changed_job:
            raise NotFoundError(self.name, f'uid {job.uid} not found')

        changed_job.name = job.name
        changed_job.salary = job.salary
        changed_job.description = job.description
        changed_job.date_published = job.date_published
        changed_job.date_expiring = job.date_expiring
        changed_job.url = job.url

        db_session.commit()

        return CorrectJob.from_orm(changed_job)

    def get_all(self):
        return [CorrectJob.from_orm(jobs) for jobs in Job.query.all()]

    def get_by_id(self, uid):
        job = Job.query.filter(Job.uid == uid).first()
        if not job:
            raise NotFoundError(self.name, f'uid {uid} not found')

        return CorrectJob.from_orm(job)

    def get_for_company(self, uid):
        entity = Job.query.filter(Job.company_uid == uid).all()

        return [CorrectJob.from_orm(jobs) for jobs in entity]

    def get_by_url(self, company_id: int, url: str) -> CorrectJob:
        job = Job.query.filter(Job.company_uid == company_id).filter(Job.url == url).first()
        if not job:
            raise NotFoundError(self.name, f'url: {url} not found, company: {company_id}')

        return CorrectJob.from_orm(job)
