from resources.lib import main
from resources.lib import common
import xbmcgui
import sys

if __name__ == '__main__':

    torrent = sys.argv[1] if len(sys.argv) > 1 else None
    if (torrent):
        dir = sys.argv[2] if len(sys.argv) > 2 else None
        paused = sys.argv[3] if len(sys.argv) > 3 else None
        transmission = common.get_rpc_client()

        transmission.add_torrent(torrent, download_dir=dir, paused=paused == 'True')

        dialog = xbmcgui.Dialog()
        dialog.notification('Torrent Added', 'Added as paused!' if paused == 'True' else 'Added and downloading...', xbmcgui.NOTIFICATION_INFO, 5000)
    else:
        main.Main()
