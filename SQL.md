# SQL

## Tables
- Create projects table:
    `id, name`
    ```sql
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
    ```
- Create tasks table:
    `id, name, status, project_id`
    ```sql
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        status TEXT,
        project_id INTEGER,
        FOREIGN KEY (project_id) REFERENCES projects(id)
    );
    ```

## Queries
1. Get all statuses, not repeating, alphabetically ordered:
    ```sql
    SELECT DISTINCT status FROM tasks ORDER BY status ASC;
    ```
2. Get the count of all tasks in each project, order by task count descending:
    ```sql
    SELECT project.id AS project_id, COUNT(task.id) AS task_count
    FROM projects project
    LEFT JOIN tasks task ON task.project_id = project.id
    GROUP BY project.id
    ORDER BY task_count DESC;
    ```
3. Get the count of all tasks in each project, order by projects names:
    ```sql
    SELECT 
        project.id AS project_id,
        project.name AS project_name,
        COUNT(task.id) AS task_count
    FROM projects project
    LEFT JOIN tasks task ON task.project_id = project.id
    GROUP BY project.id, project.name
    ORDER BY project.name ASC;
    ```
4. Get the tasks for all projects having the name beginning with the letter 'N':
    ```sql
    SELECT task.* FROM tasks task
    JOIN projects project ON project.id = task.project_id
    WHERE project.name LIKE "N%"
    ```
5. Get the list of all projects containing the letter 'a' in the middle of the name, and show task count near each project. Mention that there can exist projects without tasks and tasks with project_id=NULL:
    ```sql
    SELECT project.id, project.name, COUNT(task.id) AS task_count
    FROM projects project
    LEFT JOIN tasks task ON task.project_id = project.id
    WHERE project.name LIKE "%a%"
    GROUP BY project.id, project.name
    ```
6. Get the list of tasks with duplicate names, order alphabetically:
    ```sql
    SELECT * FROM tasks
    WHERE name IN (
        SELECT name FROM tasks
        GROUP BY name
        HAVING COUNT(*) > 1
    )
    ORDER BY name ASC;
    ```
7. Get the list of tasks from the project 'Delivery’ that have several exact matches of both name and status, order by match count:
    ```sql
    SELECT task.* FROM tasks task
    JOIN projects project ON project.id = task.project_id
    JOIN (
        SELECT name, status, project_id, COUNT(*) as match_count FROM tasks
        GROUP BY name, status, project_id
        HAVING COUNT(*) > 1
    ) AS duplicates ON (
        duplicates.name = task.name AND 
        duplicates.status = task.status AND
        duplicates.project_id = task.project_id
    )
    WHERE project.name = "Delivery"
    ORDER BY duplicates.match_count DESC;
    ```
8. Get the list of project names having more than 10 tasks with status 'completed', order by project_id:
    ```sql
    SELECT project.* FROM projects project
    JOIN tasks task ON task.project_id = project.id
    WHERE task.status = "completed"
    GROUP BY project.id, project.name
    HAVING COUNT(task.id) > 10
    ORDER BY project.id ASC;
    ```
