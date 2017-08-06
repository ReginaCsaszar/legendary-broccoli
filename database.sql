ALTER TABLE IF EXISTS ONLY users DROP CONSTRAINT IF EXISTS pk_users_id CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;
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


ALTER TABLE IF EXISTS ONLY teams DROP CONSTRAINT IF EXISTS fk_teams_scrum_id;
ALTER TABLE IF EXISTS ONLY teams DROP CONSTRAINT IF EXISTS pk_teams_id CASCADE;
DROP TABLE IF EXISTS teams CASCADE;
DROP SEQUENCE IF EXISTS teams_id_seq;
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


ALTER TABLE IF EXISTS ONLY members DROP CONSTRAINT IF EXISTS fk_members_user_id;
ALTER TABLE IF EXISTS ONLY members DROP CONSTRAINT IF EXISTS fk_members_team_id;
ALTER TABLE IF EXISTS ONLY members DROP CONSTRAINT IF EXISTS pk_members_id CASCADE;
DROP TABLE IF EXISTS members CASCADE;
DROP SEQUENCE IF EXISTS members_id_seq;
CREATE TABLE members (
    id SERIAL NOT NULL,
    user_id integer NOT NULL,
    team_id integer NOT NULL
);
ALTER TABLE ONLY members ADD CONSTRAINT pk_members_id PRIMARY KEY (id);
ALTER TABLE ONLY members ADD CONSTRAINT fk_members_user_id FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE;
ALTER TABLE ONLY members ADD CONSTRAINT fk_members_team_id FOREIGN KEY (team_id) REFERENCES teams(id) ON DELETE CASCADE;


ALTER TABLE IF EXISTS ONLY projects DROP CONSTRAINT IF EXISTS fk_projects_owner_id;
ALTER TABLE IF EXISTS ONLY projects DROP CONSTRAINT IF EXISTS fk_tasks_project_id;
ALTER TABLE IF EXISTS ONLY projects DROP CONSTRAINT IF EXISTS pk_projects_id;
DROP TABLE IF EXISTS projects CASCADE;
DROP SEQUENCE IF EXISTS projects_id_seq;
CREATE TABLE projects (
    id SERIAL NOT NULL,
    title character varying(100) NOT NULL,
    description character varying(2000),
    status character varying(7) DEFAULT 'created',
    owner_id integer NOT NULL,
    team_id integer,
    created_date TIMESTAMP(0) DEFAULT LOCALTIMESTAMP(0),
    start_time TIMESTAMP(0),
    due_date TIMESTAMP(0),
    spent_time interval(0)
);
ALTER TABLE ONLY projects ADD CONSTRAINT pk_projects_id PRIMARY KEY (id);
ALTER TABLE ONLY projects ADD CONSTRAINT fk_projects_owner_id FOREIGN KEY (owner_id) REFERENCES users(id) ON DELETE CASCADE;
ALTER TABLE ONLY projects ADD CONSTRAINT fk_projects_team_id FOREIGN KEY (team_id) REFERENCES teams(id) ON DELETE CASCADE;


ALTER TABLE IF EXISTS ONLY tasks DROP CONSTRAINT IF EXISTS fk_tasks_project_id;
ALTER TABLE IF EXISTS ONLY tasks DROP CONSTRAINT IF EXISTS fk_tasks_owner_id;
ALTER TABLE IF EXISTS ONLY tasks DROP CONSTRAINT IF EXISTS pk_tasks_id CASCADE;
DROP TABLE IF EXISTS tasks CASCADE;
DROP SEQUENCE IF EXISTS tasks_id_seq;
CREATE TABLE tasks (
    id SERIAL NOT NULL,
    title character varying(100) NOT NULL,
    description character varying(2000),
    project_id integer NOT NULL,
    owner_id integer NOT NULL,
    status character varying(7) DEFAULT 'created',
    created_date TIMESTAMP(0) DEFAULT LOCALTIMESTAMP(0),
    start_time TIMESTAMP(0),
    due_date TIMESTAMP(0),
    spent_time interval(0)
);
ALTER TABLE ONLY tasks ADD CONSTRAINT pk_tasks_id PRIMARY KEY (id);
ALTER TABLE ONLY tasks ADD CONSTRAINT fk_tasks_project_id FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE;
ALTER TABLE ONLY tasks ADD CONSTRAINT fk_tasks_owner_id FOREIGN KEY (owner_id) REFERENCES users(id) ON DELETE CASCADE;


ALTER TABLE IF EXISTS ONLY checklists DROP CONSTRAINT IF EXISTS fk_checklists_task_id;
ALTER TABLE IF EXISTS ONLY checklists DROP CONSTRAINT IF EXISTS pk_checklists_id CASCADE;
DROP TABLE IF EXISTS checklists CASCADE;
DROP SEQUENCE IF EXISTS checklists_id_seq;
CREATE TABLE checklists (
    id SERIAL NOT NULL,
    task_id integer NOT NULL,
    description character varying(2000),
    status boolean DEFAULT FALSE
);
ALTER TABLE ONLY checklists ADD CONSTRAINT pk_checklists_id PRIMARY KEY (id);
ALTER TABLE ONLY checklists ADD CONSTRAINT fk_checklists_task_id FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE;


ALTER TABLE IF EXISTS ONLY timers DROP CONSTRAINT IF EXISTS fk_timers_task_id;
ALTER TABLE IF EXISTS ONLY timers DROP CONSTRAINT IF EXISTS pk_timers_id CASCADE;
DROP TABLE IF EXISTS timers CASCADE;
DROP SEQUENCE IF EXISTS timers_id_seq;
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
INSERT INTO teams (name, overview, scrum_id) VALUES ('Bits Please!', 'Team for testing the page', '1');
INSERT INTO members (user_id, team_id) VALUES ('1', '1');
INSERT INTO members (user_id, team_id) VALUES ('2', '1');
INSERT INTO members (user_id, team_id) VALUES ('3', '1');
INSERT INTO members (user_id, team_id) VALUES ('4', '1');
INSERT INTO projects (title, description, owner_id, team_id, due_date) VALUES ('Feed cats', 'It is time to feed cats', '1', '1', NOW());
INSERT INTO projects (title, description, owner_id, due_date) VALUES ('Feed cats more', 'There are another time to feed cats', '1', NOW());
INSERT INTO projects (title, description, owner_id, team_id, due_date) VALUES ('Feed family', 'It is time to feed us', '2', '1', NOW());
INSERT INTO projects (title, description, owner_id, team_id, due_date) VALUES ('Go on holiday', 'It is time to go on holiday', '2', '1', NOW());
INSERT INTO tasks (title, description, project_id, owner_id) VALUES ('Booking holiday', 'Reserve rooms', 4, 2);
INSERT INTO tasks (title, description, project_id, owner_id) VALUES ('Buy train tickets', 'As fast as can', 4, 2);
