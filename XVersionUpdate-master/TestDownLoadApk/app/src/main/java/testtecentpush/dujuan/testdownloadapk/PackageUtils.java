package testtecentpush.dujuan.testdownloadapk;

import android.app.Activity;
import android.content.pm.PackageInfo;
import android.content.pm.PackageManager;

/**
 * Created by dujuan on 2017/11/22.
 */

class PackageUtils {
    public static int getVersionCode(Activity mainActivity) throws PackageManager.NameNotFoundException {
        // 获取packagemanager的实例
        PackageManager packageManager = mainActivity.getPackageManager();
        // getPackageName()是你当前类的包名，0代表是获取版本信息
        PackageInfo packInfo = packageManager.getPackageInfo(mainActivity.getPackageName(),0);
        String version = packInfo.versionName;
        int ver = Integer.parseInt(version);
        return ver;
    }


}
