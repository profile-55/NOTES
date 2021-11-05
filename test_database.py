# -*- coding: utf-8 -*-

import models
from database import SessionLocal


if __name__ == '__main__':

    db = SessionLocal()
    tasks = db.query(models.Task).all()
    print(tasks)