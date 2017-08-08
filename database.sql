ALTER TABLE IF EXISTS ONLY users DROP CONSTRAINT IF EXISTS pk_users_id CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;

ALTER TABLE IF EXISTS ONLY teams DROP CONSTRAINT IF EXISTS fk_teams_scrum_id;
ALTER TABLE IF EXISTS ONLY teams DROP CONSTRAINT IF EXISTS pk_teams_id CASCADE;
DROP TABLE IF EXISTS teams CASCADE;
DROP SEQUENCE IF EXISTS teams_id_seq;

ALTER TABLE IF EXISTS ONLY members DROP CONSTRAINT IF EXISTS fk_members_user_id;
ALTER TABLE IF EXISTS ONLY members DROP CONSTRAINT IF EXISTS fk_members_team_id;
ALTER TABLE IF EXISTS ONLY members DROP CONSTRAINT IF EXISTS pk_members_id CASCADE;
DROP TABLE IF EXISTS members CASCADE;
DROP SEQUENCE IF EXISTS members_id_seq;

ALTER TABLE IF EXISTS ONLY projects DROP CONSTRAINT IF EXISTS fk_projects_owner_id;
ALTER TABLE IF EXISTS ONLY projects DROP CONSTRAINT IF EXISTS fk_tasks_project_id;
ALTER TABLE IF EXISTS ONLY projects DROP CONSTRAINT IF EXISTS pk_projects_id CASCADE;
DROP TABLE IF EXISTS projects CASCADE;
DROP SEQUENCE IF EXISTS projects_id_seq;

ALTER TABLE IF EXISTS ONLY tasks DROP CONSTRAINT IF EXISTS fk_tasks_project_id;
ALTER TABLE IF EXISTS ONLY tasks DROP CONSTRAINT IF EXISTS fk_tasks_owner_id;
ALTER TABLE IF EXISTS ONLY tasks DROP CONSTRAINT IF EXISTS pk_tasks_id CASCADE;
DROP TABLE IF EXISTS tasks CASCADE;
DROP SEQUENCE IF EXISTS tasks_id_seq;

ALTER TABLE IF EXISTS ONLY checklists DROP CONSTRAINT IF EXISTS fk_checklists_task_id;
ALTER TABLE IF EXISTS ONLY checklists DROP CONSTRAINT IF EXISTS pk_checklists_id CASCADE;
DROP TABLE IF EXISTS checklists CASCADE;
DROP SEQUENCE IF EXISTS checklists_id_seq;

ALTER TABLE IF EXISTS ONLY timers DROP CONSTRAINT IF EXISTS fk_timers_task_id;
ALTER TABLE IF EXISTS ONLY timers DROP CONSTRAINT IF EXISTS pk_timers_id CASCADE;
DROP TABLE IF EXISTS timers CASCADE;
DROP SEQUENCE IF EXISTS timers_id_seq;

CREATE TABLE users (
    id SERIAL NOT NULL,
    name character varying(100) NOT NULL UNIQUE,
    password character varying(100) NOT NULL,
    registration_date TIMESTAMP(0) DEFAULT LOCALTIMESTAMP(0),
    lastlogin TIMESTAMP(0) DEFAULT LOCALTIMESTAMP(0),
    settings character varying(100) DEFAULT 'light',
    avatar_link character varying(2000)
);
ALTER TABLE ONLY users ADD CONSTRAINT pk_users_id PRIMARY KEY (id);

CREATE TABLE teams (
    id SERIAL NOT NULL,
    name character varying(100) NOT NULL UNIQUE,
    overview character varying(2000),
    created_date TIMESTAMP DEFAULT LOCALTIMESTAMP(0),
    scrum_id integer,
    logo character varying(2000)
);
ALTER TABLE ONLY teams ADD CONSTRAINT pk_teams_id PRIMARY KEY (id);
ALTER TABLE ONLY teams ADD CONSTRAINT fk_teams_scrum_id FOREIGN KEY (scrum_id) REFERENCES users(id) ON DELETE CASCADE;

CREATE TABLE members (
    id SERIAL NOT NULL,
    user_id integer NOT NULL,
    team_id integer NOT NULL
);
ALTER TABLE ONLY members ADD CONSTRAINT pk_members_id PRIMARY KEY (id);
ALTER TABLE ONLY members ADD CONSTRAINT fk_members_user_id FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE;
ALTER TABLE ONLY members ADD CONSTRAINT fk_members_team_id FOREIGN KEY (team_id) REFERENCES teams(id) ON DELETE CASCADE;

CREATE TABLE projects (
    id SERIAL NOT NULL,
    title character varying(100) NOT NULL,
    description character varying(2000),
    status character varying(7) DEFAULT 'created',
    owner_id integer NOT NULL,
    team_id integer,
    creation_date TIMESTAMP(0) DEFAULT LOCALTIMESTAMP(0),
    modification_date TIMESTAMP(0),
    goal_time interval(0) DEFAULT '40 hours',
    due_date TIMESTAMP(0) DEFAULT LOCALTIMESTAMP(0) + '5 days',
    spent_time interval(0) DEFAULT '0'
);
ALTER TABLE ONLY projects ADD CONSTRAINT pk_projects_id PRIMARY KEY (id);
ALTER TABLE ONLY projects ADD CONSTRAINT fk_projects_owner_id FOREIGN KEY (owner_id) REFERENCES users(id) ON DELETE CASCADE;
ALTER TABLE ONLY projects ADD CONSTRAINT fk_projects_team_id FOREIGN KEY (team_id) REFERENCES teams(id) ON DELETE CASCADE;


CREATE TABLE tasks (
    id SERIAL NOT NULL,
    title character varying(100) NOT NULL,
    description character varying(2000),
    project_id integer NOT NULL,
    owner_id integer,
    status character varying(7) DEFAULT 'created',
    creation_date TIMESTAMP(0) DEFAULT LOCALTIMESTAMP(0),
    modification_date TIMESTAMP(0),
    due_date TIMESTAMP(0) DEFAULT LOCALTIMESTAMP(0) + '3 days',
    goal_time interval(0) DEFAULT '4 hours',
    spent_time interval(0) DEFAULT '0'
);
ALTER TABLE ONLY tasks ADD CONSTRAINT pk_tasks_id PRIMARY KEY (id);
ALTER TABLE ONLY tasks ADD CONSTRAINT fk_tasks_project_id FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE;
ALTER TABLE ONLY tasks ADD CONSTRAINT fk_tasks_owner_id FOREIGN KEY (owner_id) REFERENCES users(id) ON DELETE CASCADE;

CREATE TABLE checklists (
    id SERIAL NOT NULL,
    task_id integer NOT NULL,
    description character varying(100),
    status boolean DEFAULT FALSE
);
ALTER TABLE ONLY checklists ADD CONSTRAINT pk_checklists_id PRIMARY KEY (id);
ALTER TABLE ONLY checklists ADD CONSTRAINT fk_checklists_task_id FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE;

CREATE TABLE timers (
    id SERIAL NOT NULL,
    task_id integer NOT NULL,
    start_time TIMESTAMP(0),
    stop_time TIMESTAMP(0)
);
ALTER TABLE ONLY timers ADD CONSTRAINT pk_timers_id PRIMARY KEY (id);
ALTER TABLE ONLY timers ADD CONSTRAINT fk_timers_task_id FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE;


INSERT INTO users (name, password) VALUES ('Jeannie', 'admin');
INSERT INTO users (name, password) VALUES ('Kékúr', 'admin');
INSERT INTO users (name, password) VALUES ('Beni', 'admin');
INSERT INTO users (name, password) VALUES ('Mira', 'admin');
INSERT INTO teams (name, overview, scrum_id) VALUES ('Bits Please!', 'Team for testing the page', 1);
INSERT INTO members (user_id, team_id) VALUES (1, 1);
INSERT INTO members (user_id, team_id) VALUES (2, 1);
INSERT INTO members (user_id, team_id) VALUES (3, 1);
INSERT INTO members (user_id, team_id) VALUES (4, 1);

INSERT INTO projects (title, description, status, owner_id, team_id, goal_time, due_date, spent_time)
VALUES ('The first project of the team', '', 'Active', 1, 1, '20 hour', LOCALTIMESTAMP(0) + '14 days', '9851 seconds');
INSERT INTO projects (title, description, status, owner_id, team_id, goal_time, due_date, spent_time)
VALUES ('The second project of the team', '', 'Active', 2, 1, '15 hour', LOCALTIMESTAMP(0) + '10 days', '156 seconds');
INSERT INTO projects (title, description, status, owner_id, team_id, goal_time, due_date, spent_time)
VALUES ('The third project of the team', '', 'Done', 1, 1, '5 hour', LOCALTIMESTAMP(0) + '3 days', '16000 seconds');
INSERT INTO projects (title, description, status, owner_id, team_id, goal_time, due_date, spent_time)
VALUES ('The fourth project of the team', '', 'Done', 2, 1, '50 hour', LOCALTIMESTAMP(0) + '30 days', '124351 seconds');
INSERT INTO projects (title, description, status, owner_id, team_id, goal_time, due_date, spent_time)
VALUES ('The first personal project of me', '', 'Active', 1, NULL, '40 hour', LOCALTIMESTAMP(0) + '3 days', '1685 seconds');
INSERT INTO projects (title, description, status, owner_id, team_id, goal_time, due_date, spent_time)
VALUES ('The second personal project of me', '', 'Active', 1, NULL, '40 hour', LOCALTIMESTAMP(0) + '1 days', '10000 seconds');
INSERT INTO projects (title, description, status, owner_id, team_id, goal_time, due_date, spent_time)
VALUES ('The third personal project of me', '', 'Done', 1, NULL, '1 hour', LOCALTIMESTAMP(0) + '3 days', '3520 seconds');
INSERT INTO projects (title, description, status, owner_id, team_id, goal_time, due_date, spent_time)
VALUES ('The first personal project of other team member', '', 'Active', 1, NULL, '40 hour', LOCALTIMESTAMP(0) + '3 days', '1685 seconds');


INSERT INTO tasks (title, description, project_id, owner_id, status, due_date, goal_time, spent_time) 
VALUES ('The first task of the team', '', 1, 1, 'Active', LOCALTIMESTAMP(0) + '14 days', '5 hour', '11000');
INSERT INTO tasks (title, description, project_id, owner_id, status, due_date, goal_time, spent_time) 
VALUES ('The secondt task of the team', '', 1, 1, 'Done', LOCALTIMESTAMP(0) + '14 days', '3 hour', '9000');
INSERT INTO tasks (title, description, project_id, owner_id, status, due_date, goal_time, spent_time) 
VALUES ('The third task of the team', '', 2, 1, 'Active', LOCALTIMESTAMP(0) + '14 days', '5 hour', '13000');
INSERT INTO tasks (title, description, project_id, owner_id, status, due_date, goal_time, spent_time) 
VALUES ('The fourth task of the team', '', 2, 1, 'Done', LOCALTIMESTAMP(0) + '14 days', '5 hour', '15000');
INSERT INTO tasks (title, description, project_id, owner_id, due_date, goal_time) 
VALUES ('The fifth task of the team', '', 0, 1, LOCALTIMESTAMP(0) + '10 days', '2 hour');

INSERT INTO tasks (title, description, project_id, owner_id, status, due_date, goal_time, spent_time) 
VALUES ('The first personal task of me', '', 5, 1, 'Done', LOCALTIMESTAMP(0) + '1 day', '5 hour', '15000');
INSERT INTO tasks (title, description, project_id, owner_id, status, due_date, goal_time, spent_time) 
VALUES ('The second personal task of me', '', 5, 1, 'Active', LOCALTIMESTAMP(0) + '3 days', '15 hour', '17000');
INSERT INTO tasks (title, description, project_id, owner_id, status, due_date, goal_time, spent_time) 
VALUES ('The third personal task of me', '', 5, 1, 'Active', LOCALTIMESTAMP(0) + '2 days', '10 hour', '9000');
INSERT INTO tasks (title, description, project_id, owner_id, due_date, goal_time) 
VALUES ('The fourth personal task of me', '', 5, 1, LOCALTIMESTAMP(0) + '3 days', '10 hour');