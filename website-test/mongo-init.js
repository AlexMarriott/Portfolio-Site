var password = "Movingonup2020";
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