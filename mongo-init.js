var password = "MONGO_INITDB_ROOT_PASSWORD";
db.createUser(
        {
            user: "alex",
            pwd: password,
            roles: [
                {
                    role: "readWrite",
                    db: "projects"
                }
            ]
        }
);