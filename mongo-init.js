var password = "MONGO_INITDB_ROOT_PASSWORD";
db.createUser(
        {
            user: "root",
            pwd: password,
            roles: [
                {
                    role: "readWrite",
                    db: "projects"
                }
            ]
        }
);