#!/usr/bin/env python

class AllLogsConverter(object):
    """
    Convert all json file for each user to one coordinated file for each user.
    """

    # base directory and paths
    # base_path = "/data/mixs_logs/"
    # for widget logger
    base_path = "/speech/dbwork/mul/reco1/AppPrediction/SonyLogging/Logs/from_TKY/pulled_from_TKY/mixs_logs/"
    # for launcher logger
    #base_path = "/speech/dbwork/mul/reco1/AppPrediction/SonyLogging/Logs/from_TKY/pulled_from_TKY/mixs_launcher_logs/"

    json_log_dir = "json"
    all_in_one_log_dir = "all"
    all_in_one_json_file = "all_in_one_log.json"
    all_in_one_gvc_tljs_file = "gvc_tljs_log.json"

    usrs_dir = "usrs"
    apps_dir = "apps"
    stats_dir = "stats"
    json_log_path = "%s/%s" % (base_path, json_log_dir)
    json_usrs_log_path = "%s/%s/%s" % (base_path, json_log_dir, usrs_dir)
    json_apps_log_path = "%s/%s/%s" % (base_path, json_log_dir, apps_dir)
    stats_log_path = "%s/%s/%s" % (base_path, json_log_dir, stats_dir)
    
    usrs = "usrs"
    usr_stats = "usr_stats.json"
    app_stats = "app_stats.json"
    
    # hdfs setting
    user = "mixs"
    hdfs_user_root = "/user/%s" % (user)
    mnt_point = "/mnt/hdfs/"
    hdfs_base_path = "%s/user/mixs/data/mixs_logs" % (mnt_point)
    hdfs_json_log_path = "%s/%s" % (hdfs_base_path, json_log_dir)
    hdfs_all_in_one_log_dir = all_in_one_log_dir
    hdfs_in_one_log_file = all_in_one_json_file
    
    # key
    APP_INFO = "appInfo"
    BASE_INFO = "baseInfo"
    LOG_INFO = "logInfo"
    EVENT = "event"
    SEQ = "seq"
    TIME = "time"
    APP_LAUNCH= "appLaunch"
    APP_NAME = "appName"
    LOCATION = "location"
    TIMEZONE = "timeZone"
    UUID = "db_key_uuid"
    IMEI = "db_key_device_id"
    KEY = "key"
    VALUE = "value"
    
    WIFI_APS = "wifiAps"
    WIFI_CONNECTED_AP = "wifiConnectedAp"
    SENSOR = "sensor"
    BLUETOOTH = "bluetooth"
    BATTERY = "battery"
    HEADSET_PLUG = "headsetPlug"
    NETWORK_INFO = "networkInfo"
    TELEPHONY = "telephony"
    NEIGHBORING_CELL_INFO = "neighboringCellInfo"

    STATS = "stats"
    
    def __init__(self, json_log_path = json_log_path):
        """
        init

        
        - `filename`: filname created unser
        """
        self.json_log_path = json_log_path
        pass
