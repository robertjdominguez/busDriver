from app import *
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, flash

# Inputs for new driver
d_first = input('First name:\n')
l_name = input('Last name:\n')
cell = input('Number:\n')
mom_name = input("Mother's name:\n")
dad_name = input("Dad's name:\n")
mom_num = input("Mom's number:\n")
dad_num = input("Dad's number:\n")

new_student = Students(first_name=d_first,
                    last_name=l_name,
                    c_num=cell,
                    m_name = mom_name,
                    f_name = dad_name,
                    m_num = mom_num,
                    f_num = dad_num,
                    )

db.session.add(new_student)
db.session.commit()
