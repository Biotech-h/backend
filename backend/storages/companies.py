from sqlalchemy.exc import IntegrityError

from backend.database.db import db_session
from backend.database.models import Company, Job
from backend.errors import ConflictError, NotFoundError
from backend.schemas.company import CorrectCompany
from backend.schemas.job import CorrectJob


class CompaniesStorage():
    name = 'Companies'

    def add(self, company: CorrectCompany):
        new_company = Company(
            name=company.name,
            region=company.region,
            category=company.category,
            description=company.description,
        )
        db_session.add(new_company)
        db_session.commit()

        return CorrectCompany.from_orm(new_company)

    def delete(self, uid):
        company = Company.query.filter(Company.uid == uid).first()
        if not company:
            raise NotFoundError(self.name, f'uid {uid} not found')

        db_session.delete(company)

        try:
            db_session.commit()
        except IntegrityError:
            raise ConflictError(self.name, 'can not delete company with jobs')

    def update(self, company: CorrectCompany):
        changed_company = Company.query.filter(Company.uid == company.uid).first()
        if not changed_company:
            raise NotFoundError(self.name, f'uid {company.uid} not found')

        changed_company.name = company.name
        changed_company.region = company.region
        changed_company.category = company.category
        changed_company.description = company.description

        db_session.commit()

        return CorrectCompany.from_orm(changed_company)

    def get_all(self):
        return [CorrectCompany.from_orm(companies) for companies in Company.query.all()]

    def get_by_id(self, uid):
        company = Company.query.filter(Company.uid == uid).first()
        if not company:
            raise NotFoundError(self.name, f'uid {uid} not found')

        return CorrectCompany.from_orm(company)

    def get_jobs_by_company_id(self, uid):
        entity = Job.query.filter(Job.company_uid == uid).all()
        if not entity:
            raise NotFoundError(self.name, f'jobs with company uid {uid} does not exist')

        return [CorrectJob.from_orm(jobs) for jobs in entity]
