from odoo import models,api, fields
import datetime
class Courses(models.Model):
    _name="academy.courses"
    _description="Course records"
    
    name=fields.Char(string='Course title:',required=True)
    price=fields.Integer(string='Course Price', required=True)
    group_ids = fields.One2many('academy.groups', 'course_id',)


class Mentors(models.Model):
    _name="academy.mentors"
    _description="Mentors records"
    

    name=fields.Char(string='Mentor name',required=True)
    age=fields.Integer(string='Age', )
    subject=fields.Char(string='Subject', required=True)
    experience=fields.Char(string='Experience', required=True)
    group_ids=fields.One2many('academy.groups','mentor_id',)
    payment=fields.One2many('academy.payment_mentor', 'mentor_id', string='Salary list')

class Students(models.Model):
    _name="academy.students"
    _description="Student records"

    name=fields.Char(string='Name',required=True)
    age=fields.Integer(string='Age',required=True)
    phone=fields.Char(string='Phone number', required=True)
    group_ids=fields.Many2many('academy.groups',)
    payment_ids=fields.One2many('academy.payment_student','student_id')
    
class Groups(models.Model):
    """
    We can create groups for particular subjects and students 
    by cooparating a mentor via this class  
    """
    _name="academy.groups"
    _description="Group records"
    _rec_name="group_name"

    group_name=fields.Char(string="Group title:", required=True,)
    course_id = fields.Many2one('academy.courses', string='Course title:')
    mentor_id=fields.Many2one('academy.mentors',ondelete='cascade' )
    student_ids=fields.Many2many('academy.students', string='Students No:')
    mentor_name=fields.Char(string="Mentor name:",required=True, related='mentor_id.name')
                                    

class PaymentStudent(models.Model):
    """
    Students can make payment for particular subject groups 
    """
    _name="academy.payment_student"
    _description="Student payment records"
   
    student_id=fields.Many2one('academy.students', string='Student name:',ondelete='cascade')
    name=fields.Char(string='Student name',required=True, related='student_id.name')
    group_ids=fields.Many2many('academy.groups', string="Groups")
    first_day=fields.Date(string='first day', required=True)
    last_day=fields.Date(string='last day', required=True)
    tuition_fee=fields.Integer(string='Tuiton Fee',required=True,)

            

class PaymentMentor(models.Model):
    _name="academy.payment_mentor"
    _description="Mentor paymnet records"
    rec_name="mentor_name"
    
    mentor_id=fields.Many2one('academy.mentors', string='Mentor name',ondelete='cascade')
    mentor_name=fields.Char(string="Mentor name:",required=True, related='mentor_id.name')
    salary_amount=fields.Integer(string='Mentor salary',required=True,)
    
    


    