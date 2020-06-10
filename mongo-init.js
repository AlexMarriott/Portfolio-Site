db.createUser(
        {
            user: "alex",
            pwd: "",
            roles: [
                {
                    role: "readWrite",
                    db: "projects"
                }
            ]
        }
);