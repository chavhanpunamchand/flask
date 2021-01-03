from flask import request
from AcademyREST_API.producer.config import db
import json
from AcademyREST_API.producer.service import ApplicationServices
from AcademyREST_API.producer.models import Student


class StudentServiceImpl(ApplicationServices):  # actual implementations

    def add_entity(self,stud):
        if type(stud) == Student:
            db.session.add(stud)
            db.session.commit()
            print('Student Added')
            return True
        print('Invalid Student')
        return False

    def remove_entity(self,stdid):
        dbstud = self.fetch_entity(stdid)
        if dbstud:
            db.session.delete(dbstud)
            db.session.commit()
            print('Student Removed')
            return True
        print('No Student with given Id cannot remove')
        return False

    def update_entity(self, stdid, stud):
        dbstud = self.fetch_entity(stdid)
        if dbstud:
            dbstud.fullname = stud.fullname
            dbstud.age = stud.age
            dbstud.email = stud.email
            dbstud.photo = stud.photo
            db.session.commit()
            print('student Updated succefully...')
            return self.fetch_entity(stdid)
        print('No student..cannot update..')

    def fetch_entity(self, stdid):
        if type(stdid) == int and stdid > 0:
            stud = Student.query.filter_by(id=stdid).first()
            if stud:
                return stud

    def fetch_all_entities(self):
        return Student.query.all()
