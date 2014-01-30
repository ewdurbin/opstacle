import datetime
import collections
import threading

class ExpireCounter:
    """Tracks how many events were added in the preceding time period
    """

    def __init__(self, timeout=1):
        self.lock=threading.Lock()        
        self.timeout = timeout
        self.events = collections.deque()

    def add(self,item):
        """Add event time
        """
        with self.lock:
            self.events.append(item)
            threading.Timer(self.timeout,self.expire).start()

    def __len__(self):
        """Return number of active events
        """
        with self.lock:
            return len(self.events)

    def expire(self):
        """Remove any expired events
        """
        with self.lock:
            self.events.popleft()

    def __str__(self):
        with self.lock:
            return str(self.events)
