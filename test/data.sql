/**

    Cass Johnston (cassjohnston@gmail.com) 2012-02-12

    This script will populate a new piman mysql database with some test data. 
    Create the database, then run the python manage.py syncdb script. When asked
    if you want to create an admin user, say no - this script will do it for you.

**/

/* Django stores passwords as algorithm$salt$hash in the database: */

DELIMITER //
CREATE FUNCTION django_password(
  pass VARCHAR(32)
) RETURNS VARCHAR(128) 
BEGIN
  DECLARE salt char(5);
  DECLARE hash VARCHAR(40);
  SET salt = MID(RAND(), 3, 5);
  SET hash = SHA(CONCAT(salt, pass));
  RETURN CONCAT('sha1$', salt, '$', hash);
END//

DELIMITER ;

/*
  Some notes on authentication and access controls: 

  Access to the admin interface is controlled through django's standard user auth stuff with is_staff and is_superuser. 
  Only the admin user actually has access to this.

  Access to piman pages is controlled by groups and whether or not the account is a manager or a PI. 
  A PI only has access to their own information.
  If a Manager is in a group, they have access to all of the information for all of the PIs in that group.
  Managers and PIs can be members of multiple groups
  
  The pis_groupinfo table is just an extension of the built-in auth_groups table to add extra information

 */

/* admin - superuser, has access to everything through the admin interface */
insert into auth_user (id, username, first_name, last_name,email,password,is_staff, is_active,is_superuser,date_joined, last_login) values (1, 'admin','', '','comp-bio@kcl.ac.uk',django_password('password'),1,1,1,NOW(),NOW());


/* User Groups */
insert into auth_group (id, name) values (1, 'a');
insert into pis_groupinfo(id, group_id,  description) values (1,1,'this is test department A');
insert into auth_group (id, name) values (2, 'b');
insert into pis_groupinfo(id, group_id,  description) values (2,2, 'this is test department B');
insert into auth_group (id, name) values (3, 'c');
insert into pis_groupinfo(id, group_id, description) values (3,3, 'this is test department C');
insert into auth_group (id, name) values (4, 'd');
insert into pis_groupinfo(id, group_id,  description) values (4,4,'this is test department D');



/* manager_a - a manager with access to members of group a*/
insert into auth_user (id, username, first_name, last_name,email,password,is_staff, is_active,is_superuser,date_joined, last_login) values (2, 'manager_a','', '','comp-bio@kcl.ac.uk',django_password('password'),0,1,0,NOW(),NOW());
insert into pis_manager(id, user_id) values (1,2);
insert into auth_user_groups(id, user_id, group_id) values (1,2,1);


/* manager_bc - a manager with access to members of groups b and c */
insert into auth_user (id, username, first_name, last_name,email,password,is_staff, is_active,is_superuser,date_joined, last_login) values (3, 'manager_bc','', '','comp-bio@kcl.ac.uk',django_password('password'),0,1,0,NOW(),NOW());
insert into pis_manager(id,user_id) values (2, 3);
insert into auth_user_groups(id, user_id, group_id) values (2,3,3);
insert into auth_user_groups(id, user_id, group_id) values (3,3,4);


/* manager_d - a manager with access to members of group d */
insert into auth_user (id, username, first_name, last_name,email,password,is_staff, is_active,is_superuser,date_joined, last_login) values (4, 'manager_d','', '','comp-bio@kcl.ac.uk',django_password('password'),0,1,0,NOW(),NOW());
insert into pis_manager(id,user_id) values (3,4);
insert into auth_user_groups(id, user_id, group_id) values(4,4,4);





/* Create some ranks for PIs */

insert into pis_rank (id,name,description) values (1,'Lecturer','');
insert into pis_rank (id,name,description) values (2,'Senior Lecturer','');
insert into pis_rank (id,name,description) values (3,'Reader','');
insert into pis_rank (id,name,description) values (4,'Professor','');


/* PIa1 - A PI and member of group a */
insert into auth_user (id, username, first_name, last_name, email, password, is_staff, is_active, is_superuser, date_joined, last_login) values (5, 'pi_a1','PI','A1','comp-bio@kcl.ac.uk', django_password('password'), 0,1,0, NOW(),NOW());
insert into pis_pi(id, user_id, title, rank_id, telephone) values (1,5,'DR','1','0207848123');
insert into auth_user_groups(id,user_id, group_id) values (5,5,1);

/* PIa2 - A PI and member of group a */
insert into auth_user (id, username, first_name, last_name, email, password,is_staff, is_active, is_superuser, date_joined, last_login) values (6,'pi_a2','PI','A2','comp-bio@kcl.ac.uk', django_password('password'), 0,1,0,NOW(),NOW());
insert into pis_pi(id, user_id, title, rank_id, telephone) values (2,6,'PROF',4, '0207848123');
insert into auth_user_groups(id, user_id, group_id) values (6,6,1);

/* PIb - A PI and member of group b */
insert into auth_user (id, username, first_name, last_name, email, password,is_staff, is_active, is_superuser, date_joined, last_login) values (7,'pi_b','PI','B','comp-bio@kcl.ac.uk', django_password('password'), 0,1,0,NOW(),NOW());
insert into pis_pi(id, user_id, title, rank_id, telephone) values (3,7,'DR',2, '0207848123');
insert into auth_user_groups(id, user_id, group_id) values (7,7,2);


/* PIbd - A PI and member of group b and d */
insert into auth_user (id, username, first_name, last_name, email, password,is_staff, is_active, is_superuser, date_joined, last_login) values (8,'pi_bd','PI','BD','comp-bio@kcl.ac.uk', django_password('password'), 0,1,0,NOW(),NOW());
insert into pis_pi(id, user_id, title, rank_id, telephone) values (4,8,'DR',3, '0207848123');
insert into auth_user_groups(id, user_id, group_id) values (8,8,2);
insert into auth_user_groups(id, user_id, group_id) values (9,8,4);


/* PIcd - A PI and member of group  and d */
insert into auth_user (id, username, first_name, last_name, email, password,is_staff, is_active, is_superuser, date_joined, last_login) values (9,'pi_cd','PI','CD','comp-bio@kcl.ac.uk', django_password('password'), 0,1,0,NOW(),NOW());
insert into pis_pi(id, user_id, title, rank_id, telephone) values (5,9,'DR',1, '0207848123');
insert into auth_user_groups(id, user_id, group_id) values (10,9,3);
insert into auth_user_groups(id, user_id, group_id) values (11,9,4);

/* PIna - A PI whose account is not active */
insert into auth_user (id, username, first_name, last_name, email, password, is_staff, is_active, is_superuser, date_joined, last_login) values (10,'pi_na','PI','NA', 'comp-bio@kcl.ac.uk', django_password('password'), 0,0,0,NOW(),NOW());


/* Academic calendar */
insert into acad_year_academicyear (id, term1_start, term1_end, term2_start, term2_end, term3_start, term3_end,notes) values (1, '2012-01-01 00:00:00', '2012-03-01 00:00:00', '2012-04-01 00:00:00', '2012-06-01 00:00:00', '2012-07-01 00:00:00', '2012-09-01 00:00:00', '');
insert into acad_year_academicyear (id, term1_start, term1_end, term2_start, term2_end, term3_start, term3_end,notes) values (2, '2013-01-01 00:00:00', '2013-03-01 00:00:00', '2013-04-01 00:00:00', '2013-06-01 00:00:00', '2013-07-01 00:00:00', '2013-09-01 00:00:00', '');
insert into acad_year_academicyear (id, term1_start, term1_end, term2_start, term2_end, term3_start, term3_end,notes) values (3, '2015-01-01 00:00:00', '2015-03-01 00:00:00', '2015-04-01 00:00:00', '2015-06-01 00:00:00', '2015-07-01 00:00:00', '2015-09-01 00:00:00', '');


/* Create some students, projects etc. */

insert into students_studylevel (id, name, description) values (1, 'MSc', 'Master of Science');
insert into students_studylevel (id, name, description) values (2, 'MRes', 'Master of Science by Research');
insert into students_studylevel (id, name, description) values (3, 'PhD', 'Doctor of Philosophy');

insert into students_student (id, name, description, start_year_id, end_year_id, level_id) values(1,'Bob Smith', 'Blurb about Bob', 1,2,1);
insert into students_student (id, name, description, start_year_id, end_year_id, level_id) values (2, 'Kate Smith', 'Blurb about Kate', 1,3,3);

insert into students_project(id, name, description, start_year_id, end_year_id, notes) values (1, 'Project 1', 'this is a test', 1,2,'');
insert into students_project(id, name, description, start_year_id, end_year_id, notes) values (2, 'Project 2', 'this is also a test', 1,3,'');

insert into students_project_students(id, project_id, student_id) values (1,1,1);
insert into students_project_students(id, project_id, student_id) values (2,2,2);

insert into students_projectpi(id, project_id, pi_id, percentage, notes) values (1,1,1,100,'');
insert into students_projectpi(id, project_id, pi_id, percentage, notes) values (2,2,2,50,'');
insert into students_projectpi(id, project_id, pi_id, percentage, notes) values (3,2,4,50,'');


/* Create some teaching responsibilities*/
insert into courses_course(id, name, description,notes) values (1,'courseA', 'This is a test course', 'blah blah blah');
insert into courses_course(id, name, description,notes) values (2,'courseB', 'This is a test course', 'blah blah blah');

insert into courses_module(id, name, description, notes, code) values (1, 'moduleA', 'test module', 'some notes about moduleA', '12345');
insert into courses_module(id, name, description, notes, code) values (2, 'moduleB', 'test module', 'some notes about moduleB', 'ABC123');

insert into courses_courseyear(id, course_id, year_id) values (1,1,1);
insert into courses_courseyear(id, course_id, year_id) values (2,1,2);
insert into courses_courseyear(id, course_id, year_id) values (3,2,1);

insert into courses_coursemodule(id, module_id, course_id, year_id, start_date, end_date) values (1,1,1,1,'2012-03-01', '2012-06-01');
insert into courses_coursemodule(id, module_id, course_id, year_id, start_date, end_date) values (2,1,2,1,'2012-03-01', '2012-06-01');
insert into courses_coursemodule(id, module_id, course_id, year_id, start_date, end_date) values (3,2,1,1,'2012-04-01','2012-06-01');

insert into courses_teachingcommitment (id, course_module_id, pi_id, contact_hours, notes) values (1,1,1,5,'some lectures about stuff');
insert into courses_teachingcommitment (id, course_module_id, pi_id, contact_hours, notes) values (2,2,1,7, 'more lectures about stuff');
insert into courses_teachingcommitment (id, course_module_id, pi_id, contact_hours, notes) values (3,1,2,4,'other lectures about other stuff');

/* Create some publications  */

insert into publications_journal (id, title, description) values (1, 'Journal of Stuff', 'this is a journal about stuff');
insert into publications_journal (id, title, description) values (2, 'Journal of Other Stuff', 'this is another journal about stuff');

insert into publications_author(id, initials, surname, pi_id) values (1,'J', 'Bloggs',NULL);
insert into publications_author(id, initials, surname, pi_id) values (2, 'A', 'Smith', NULL);
insert into publications_author(id, initials, surname, pi_id) values (3,'PI', 'A1', 1);


insert into publications_paper(id, title, abstract,journal_id, publication_date, number_of_citations,doi) values (1,'this is a paper about stuff', 'blah blah blah blah', 1, '2010-04-28', 5, '');
insert into publications_paper(id, title, abstract,journal_id, publication_date, number_of_citations, doi) values (2, 'another paper about stuff', 'blah blah blah blah', 2, '2011-12-01', 15, '');

insert into publications_publication(id, paper_id, author_id, rank) values (1,1,1,1);
insert into publications_publication(id, paper_id, author_id, rank) values (2,1,2,2);
insert into publications_publication(id, paper_id, author_id, rank) values (3,1,3,3);

insert into publications_publication(id, paper_id, author_id, rank) values (4,2,3,1);


/* Create some grants */

insert into grants_awardingbody (id, name, description) values (1,'MRC', 'Medical Research Council');
insert into grants_awardingbody (id, name, description) values (2, 'BBSRC', 'Biotechnology and Biological Sciences Research Centre');

insert into grants_grant (id, title, description, awarding_body_id) values (1,'Some grant call title', 'A description of the cal', 1);
insert into grants_grant(id, title, description, awarding_body_id) values (2, 'Some other grant call title', 'A description of the call', 1);
insert into grants_grant(id, title, description, awarding_body_id) values (3, 'Yet another grant call title', 'blah blah blah',2);


insert into grants_submittedgrant(id, grant_id, title, abstract, decision_date, estimated_start_date, estimated_end_date, funder_contribution, fEC) values (1,1,'this is a grant title', 'blah blah blah', '2011-01-01', '2011-06-01', '2015-06-01', 100000, 100000);
insert into grants_submittedgrant(id, grant_id, title, abstract, decision_date, estimated_start_date, estimated_end_date, funder_contribution, fEC) values (2,2, 'this is another grant title', 'blah blah blah', '2012-03-01', '2012-05-01', '2014-05-01', 250000,250000);

insert into grants_applicant(id, pi_id, submitted_grant_id, percentage_split) values (1,1,1,100);
insert into grants_applicant(id, pi_id, submitted_grant_id, percentage_split) values (2,1,2,50);
insert into grants_applicant(id, pi_id, submitted_grant_id, percentage_split) values (3,2,2,50);

insert into grants_awardedgrant(id,submitted_grant_id, start_date, end_date, awarded_value) values (1, 1, '2012-05-01', '2012-06-01', '250000');


