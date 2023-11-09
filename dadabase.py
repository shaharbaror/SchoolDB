import json
import threading
import multiprocessing

import concurrent.futures
import time


class DataBase :
    def __init__(self, current_data):
        self.dataBase = current_data

    def set_value(self, key, value):
        try :
            self.dataBase[key] = value
            return "sccess"
        except Exception:
            return "failed"

    def get_value(self, key):
        if key in self.dataBase:
            return self.dataBase[key]
        return None

    def remove_value(self, key):
        if key in self.dataBase:
            return self.dataBase.pop(key)
        return None


class DBToFile (DataBase):
    def __init__(self):
        try:
            with open("db.json", "r") as f:
                super().__init__(json.load(f))
        except Exception:
            print("Failed To Load DataBase, Making new one")
            super().__init__({})

    def set_value(self, key, value):
        retVal = super(DBToFile, self).set_value(key, value)
        self.update_file()

        return retVal

    def remove_value(self, key):
        retVal = super(DBToFile, self).remove_value(key)
        self.update_file()
        return retVal

    def update_file(self):
        try:
            with open("db.json", "w") as f:
                json.dump(self.dataBase, f)
        except Exception:
            print("couldnt update dataBase")

lock = multiprocessing.Semaphore(10)

class ManageThreads (DBToFile):
    def __init__(self):
        super(ManageThreads, self).__init__()
        self.is_reading = True

    def set_value(self, key, value):

        lock.acquire()
        self.is_reading = False
        retVal = super().set_value(key, value)
        lock.release()
        return retVal

    def get_value(self, key):
        if self.is_reading:
            return super(ManageThreads, self).get_value(key)
        else:

            lock.acquire()
            self.is_reading = True
            retVal = super().get_value(key)
            lock.release()
            return retVal

    def remove_value(self, key):

        lock.acquire()
        self.is_reading = False
        retVal = super().remove_value(key)
        lock.release()
        return retVal

def kill_db(tim, key, val, db, num):
    print("starting")
    while time.time() <= tim:
        pass
    print(f"{num}. setting: {db.set_value(key, val)}.")
    print(f"{num}. getting: {db.get_value('hello')}.")
    print(f"{num}. getting: {db.get_value(key)}.")
    print(f"{num}. removing: {db.remove_value('hello')}.")

def main():
    tim = time.time() + 5
    dataBase = ManageThreads()

    t1 = threading.Thread(target=kill_db, args=(tim, "ye1p", "yu1s", dataBase, "1"))
    t2 = threading.Thread(target=kill_db, args=(tim, "nope", "ne2y", dataBase, "2"))
    t3 = threading.Thread(target=kill_db, args=(tim, "yep", "yus3", dataBase, "3"))
    t4 = threading.Thread(target=kill_db, args=(tim, "nop4e", "ney", dataBase, "4"))
    t5 = threading.Thread(target=kill_db, args=(tim, "yep", "y5us", dataBase, "5"))
    t6 = threading.Thread(target=kill_db, args=(tim, "nop5e", "n6ey", dataBase, "6"))
    t7 = threading.Thread(target=kill_db, args=(tim, "yep", "yus7", dataBase, "7"))
    t8 = threading.Thread(target=kill_db, args=(tim, "nope", "ney8", dataBase, "8"))
    t9 = threading.Thread(target=kill_db, args=(tim, "9yep", "9yus", dataBase, "9"))
    t10 = threading.Thread(target=kill_db, args=(tim, "1n0ope", "ne10y", dataBase, "10"))
    t11 = threading.Thread(target=kill_db, args=(tim, "yep", "1yus1", dataBase, "11"))
    t12 = threading.Thread(target=kill_db, args=(tim, "1no3pe", "n12ey", dataBase, "12"))
    t13 = threading.Thread(target=kill_db, args=(tim, "1ye3p", "y13us", dataBase, "13"))
    t14 = threading.Thread(target=kill_db, args=(tim, "nope", "ney", dataBase, "14"))
    # for num in range(20):
    #     multiprocessing.Process(target=kill_db, args=(tim, f"nope-is-{num}", f"n{num}ey", dataBase, str(num))).start()
    # starting thread 2
    t2.start()
    # starting thread 1
    t1.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()






    print(dataBase.remove_value("hell"))

if __name__ == "__main__":
    main()
