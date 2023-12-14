from gptos.api.misc.singleton import Singleton


class Kernel(Singleton):
    window_manager: WindowManager
    memory_manager: MemoryManager
    notification_manager: NotificationManager
