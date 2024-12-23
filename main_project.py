import config
from context_manager import DatabaseConnect


def create_table():
    with DatabaseConnect(**config.database_info) as conn:
        with conn.cursor() as cursor:
            query = '''
        CREATE TABLE IF NOT EXISTS person(
            full_name VARCHAR(100),
            age INT
        );'''
            print('table created')
            cursor.execute(query)
            conn.commit()


class Person:
    def __init__(self, full_name, age):
        self.full_name = full_name
        self.age = age

    def save(self):
        with DatabaseConnect(**config.database_info) as conn:
            with conn.cursor() as cur:
                insert_person_query = '''insert into person(full_name,age)
                values (%s,%s);
                '''
                data = (self.full_name, self.age)

                cur.execute(insert_person_query, data)
                conn.commit()
                print('Person successfully saved')

    @staticmethod
    def show_all_users():
        with DatabaseConnect(**config.database_info) as conn:
            with conn.cursor() as cur:
                cur.execute('''select * from person''')
                return f'all people {cur.fetchall()}'

    @staticmethod
    def show_one_person(name: str):
        with DatabaseConnect(**config.database_info) as conn:
            with conn.cursor() as cur:
                query = '''select * from person where full_name=%s;'''
                name = name
                cur.execute(query, (name,))
                return f'info about person-{cur.fetchone()}'


create_table()
sherali = Person('sherali olimov', 25)
sherali.save()
print(Person.show_all_users())
print(Person.show_one_person('sherali olimov'))
