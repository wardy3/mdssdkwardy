import logging

log = logging.getLogger(__name__)


class System(object):
    def __init__(self, switch):
        self.__swobj = switch

    def meminfo(self):
        """
        Get kernel memory info

        :return: memory values
        :rtype: list
        :example:
            >>> system_obj = System(switch_obj)
            >>> print(system_obj.meminfo())
             [{'memtype': 'HighTotal', 'value': '1310720', 'units': 'kB'},
              {'memtype': 'HighFree',  'value': '364800',  'units': 'kB'},
              {'memtype': 'LowTotal',  'value': '760568',  'units': 'kB'},
              {'memtype': 'LowFree',   'value': '674736',  'units': 'kB'}]

        """
        cmd = "show system internal kernel meminfo"
        if out := self.__swobj.show(cmd):
            if not self.__swobj.is_connection_type_ssh():
                return out["TABLE_flogi_entry"]["ROW_flogi_entry"]  # TODO
            return out
        else:
            return {}
