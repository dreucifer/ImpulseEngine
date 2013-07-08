"""
    Copyright (c) 2013 Randy Gaul http://RandyGaul.net

    This software is provided 'as-is', without any express or implied
    warranty. In no event will the authors be held liable for any damages
    arising from the use of this software.

    Permission is granted to anyone to use this software for any purpose,
    including commercial applications, and to alter it and redistribute it
    freely, subject to the following restrictions:
      1. The origin of this software must not be misrepresented; you must not
         claim that you wrote the original software. If you use this software
         in a product, an acknowledgment in the product documentation would be
         appreciated but is not required.
      2. Altered source versions must be plainly marked as such, and must not be
         misrepresented as being the original software.
      3. This notice may not be removed or altered from any source distribution.
"""
import time
import datetime

class Clock(object):
    """Docstring for Clock """
    __m_freq = __m_start = __m_stop = __m_current = None

    def __init__(self):
        """@todo: to be defined """
        self.start()
        self.stop()

    def start(self):
        """@todo: Docstring for start"""
        self.__m_start = time.time()

    def stop(self):
        """@todo: Docstring for stop"""
        self.__m_stop = time.time()
        
    def elapsed(self):
        """@todo: Docstring for elapsed"""
        self.__m_current = time.time()
        return str(
                datetime.timedelta(
                        seconds=(self.__m_current - self.__m_start)
                    ).total_seconds())

    def difference(self):
        """@todo: Docstring for difference"""
        return str(
                datetime.timedelta(
                        seconds=(self.__m_stop - self.__m_start)
                    ).total_seconds())

    def current(self):
        """@todo: Docstring for current"""
        self.__m_current = time.time()
        return time.strftime('%H:%M:%S', time.localtime(self.__m_current))


if __name__ == "__main__":
    newclock = Clock()
    newclock.start()
    while True:
        input()
        print(newclock.current())
        print(newclock.elapsed())
