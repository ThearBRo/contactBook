```
contactBook/
├── .gitignore
├── app/
│   ├── __init__.py
│   ├── forms/
│   │   ├── __init__.py
│   │   ├── contact_form.py
│   │   └── user_form.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── contact_model.py
│   │   └── user_model.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── contact_route.py
│   │   ├── error_route.py
│   │   └── user_route.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── contact_service.py
│   │   └── user_service.py
│   └── templates/
│       ├── auth/
│       │   ├── login.html
│       │   └── register.html
│       ├── contacts.html
│       ├── errors/
│       │   ├── 404.html
│       │   └── 500.html
│       ├── layout/
│       │   └── base.html
│       └── users.html
├── config.py
├── migrations/
│   ├── README
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
│       ├── a607731fec01_add_contact.py
│       └── fc5d07e3b93c_inital.py
├── requirements.txt
├── run.py
└── tests/
    ├── __init__&.py
    ├── test_contact_model.py
    ├── test_user_contact_relation.py
    └── test_user_model.py
```
