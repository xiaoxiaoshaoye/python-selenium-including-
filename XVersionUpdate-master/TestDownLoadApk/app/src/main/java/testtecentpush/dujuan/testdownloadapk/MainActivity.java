package testtecentpush.dujuan.testdownloadapk;

import android.content.pm.PackageManager;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.os.Build;
import  android.os.Message;
import  android.os.*;
import java.io.IOException;
import  java.io.File;
import  java.io.FileOutputStream;
import java.io.InputStream;
import java.lang.reflect.Method;
import java.util.concurrent.TimeUnit;

//import com.squareup.okhttp.Call;
//import com.squareup.okhttp.Callback;
//import com.squareup.okhttp.OkHttpClient;
//import com.squareup.okhttp.Request;
//import com.squareup.okhttp.Response;
//import com.squareup.okhttp.RequestBody;
//import  com.squareup.okhttp.ResponseBody;
//import  com.squareup.okhttp.FormEncodingBuilder;

import okhttp3.OkHttpClient;

import okhttp3.*;

import  android.widget.Toast;
import  android.util.*;

import  android.app.AlertDialog;
import android.content.DialogInterface;
import  android.content.Intent;
import com.google.gson.Gson;
import  android.app.ProgressDialog;


public class MainActivity extends AppCompatActivity {
    private static final String TAG = "MainActivity";
    private final static int  REQUEST_INSTALL_CODE = 2 ;


    //获取设备名称
    private String deviceName = Build.MODEL;
    //获取设备序列号
    private String serialNumber = getSerialNumber();
    private VersionDataBean versionDataBean;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        initData();
    }

    /**
     * 初始化数据
     */
    private void initData() {
        boolean autoUpdate = PreferenceUtils.getBoolean(this, Constants.AUTO_UPDATE, true);
        if (autoUpdate) {
            //版本更新,去服务器获取最新的版本,和本地版本比较
            new Thread(new CheckServerVersion()).start();
        } else {
            //直接跳转到登录界面
            load2Login();
        }
    }
    private Handler handler = new Handler(){
        @Override
        public void handleMessage(Message msg) {
            super.handleMessage(msg);
            switch (msg.what) {
                /** 弹出提示更新的dialog   */
                case Constants.SHOW_UPDATE_DIALOG:
                    showUpdateDialog();
                    break;

                /** 提示错误    */
                case Constants.SHOW_ERROR:
                    Toast.makeText(MainActivity.this, msg.obj+"", Toast.LENGTH_LONG).show();
                    load2Login();
                    break;

                default:
                    break;
            }
        }
    };

    /**
     * 检查服务器端版本号
     */
    private class CheckServerVersion implements Runnable {
        @Override
        public void run() {
            //访问网络,获取服务器端版本号
            OkHttpClient client = new OkHttpClient.Builder()
                    .readTimeout(Constants.READ_TIMEOUT, TimeUnit.SECONDS)//设置读取超时时间
                    .writeTimeout(Constants.WRITE_TIMEOUT,TimeUnit.SECONDS)//设置写的超时时间
                    .connectTimeout(Constants.CONNECT_TIMEOUT, TimeUnit.SECONDS).build();//设置连接超时时间
//            String url = new UrlInfo(MainActivity.this).getUrl();

            String url = "http://www.baidu.com";
            if (url.equals("http://null:null")) {
                load2Login();
            } else {
                VersionDatas versionDatas = new VersionDatas();
                //对象转json
                final Gson gson = new Gson();
                String versionDatasJson = gson.toJson(versionDatas);
                //使用post进行表单(键值对)上传
                FormBody body = new FormBody.Builder().add("versionDatasJson", versionDatasJson).build();
                Request request = new Request.Builder().url(url).post(body).build();
                client.newCall(request).enqueue(new Callback() {
                    @Override
                    public void onFailure(Call call, IOException e) {
                        //如果连接超时则跳转到登录界面
                        Message msg = Message.obtain();
                        msg.what = Constants.SHOW_ERROR;
                        msg.obj = "网络异常，请检查网络配置";
                        handler.sendMessage(msg);
                    }

                    @Override
                    public void onResponse(Call call, Response response) throws IOException {
                        if (response.isSuccessful()) {
                            Log.d(TAG, "访问接口成功");
                            String json = response.body().string();
                            Log.d(TAG, "获取服务器端版本号json=   " + json);
                            // 解析json数据
                            if(versionDataBean!=null){
                                versionDataBean = gson.fromJson(json, VersionDataBean.class);
                                //获取到服务器端版本号,对比本地的版本号
                                int serverVersionCode = versionDataBean.VERSION_NO;
                                int localVersionCode = 0;
                                try {
                                    localVersionCode =PackageUtils.getVersionCode(MainActivity.this);
                                } catch (PackageManager.NameNotFoundException e) {
                                    e.printStackTrace();
                                }
                                if (serverVersionCode > localVersionCode) {
                                    //服务器端版本号大于本地版本号,弹出dialog提示更新
                                    Message showUpdateDialog = Message.obtain();
                                    showUpdateDialog.what = Constants.SHOW_UPDATE_DIALOG;
                                    handler.sendMessage(showUpdateDialog);
                                } else {
                                    //跳转到登录界面
                                    load2Login();
                                }
                            }else{
                                load2Login();
                                Log.d(TAG,"versionDatabean为空0918");
                            }
                        } else {
                            //跳转到登录界面
                            Log.d(TAG, "访问接口失败");
                            load2Login();
                        }
                    }

                });
            }
        }
    }

    /**
     * 弹出提示更新的dialog
     */
    private void showUpdateDialog() {
        AlertDialog.Builder dialog = new AlertDialog.Builder(this);
        dialog.setCancelable(false);
        dialog.setTitle("版本更新提示");
        dialog.setMessage("檢查到有最新版本,是否更新?");
        dialog.setNegativeButton("暫不更新", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                //跳转到登录界面
                load2Login();
            }
        });
        dialog.setPositiveButton("立刻更新", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                //从服务器端下载最新apk
                downloadApk();
            }
        });
        dialog.show();
    }

    /**
     * 从服务器端下载最新apk
     */
    private void downloadApk() {
        //显示下载进度
        ProgressDialog dialog = new ProgressDialog(this);
        dialog.setProgressStyle(ProgressDialog.STYLE_HORIZONTAL);
        dialog.setCancelable(false);
        dialog.show();

        //访问网络下载apk
        new Thread(new DownloadApk(dialog)).start();
    }

    /**
     * 访问网络下载apk
     */
    private class DownloadApk implements Runnable {
        private ProgressDialog dialog;
        InputStream is;
        FileOutputStream fos;

        public DownloadApk(ProgressDialog dialog) {
            this.dialog = dialog;
        }

        @Override
        public void run() {
            OkHttpClient client = new OkHttpClient();
            String url = versionDataBean.VERSION_URL;
            Request request = new Request.Builder().get().url(url).build();
            try {
                Response response = client.newCall(request).execute();
                if (response.isSuccessful()) {
                    Log.d(TAG, "开始下载apk");
                    //获取内容总长度
                    long contentLength = response.body().contentLength();
                    //设置最大值
                    dialog.setMax((int) contentLength);
                    //保存到sd卡
                    File apkFile = new File(Environment.getExternalStorageDirectory(), System.currentTimeMillis() + ".apk");
                    fos = new FileOutputStream(apkFile);
                    //获得输入流
                    is = response.body().byteStream();
                    //定义缓冲区大小
                    byte[] bys = new byte[1024];
                    int progress = 0;
                    int len = -1;
                    while ((len = is.read(bys)) != -1) {
                        try {
                            Thread.sleep(1);
                            fos.write(bys, 0, len);
                            fos.flush();
                            progress += len;
                            //设置进度
                            dialog.setProgress(progress);
                        } catch (InterruptedException e) {
                            Message msg = Message.obtain();
                            msg.what = Constants.SHOW_ERROR;
                            msg.obj = "ERROR:10002";
                            handler.sendMessage(msg);
                            load2Login();
                        }
                    }
                    //下载完成,提示用户安装
                    installApk(apkFile);
                }
            } catch (IOException e) {
                Message msg = Message.obtain();
                msg.what = Constants.SHOW_ERROR;
                msg.obj = "ERROR:10003";
                handler.sendMessage(msg);
                load2Login();
            } finally {
                //关闭io流
                if (is != null) {
                    try {
                        is.close();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                    is = null;
                }
                if (fos != null) {
                    try {
                        fos.close();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                    fos = null;
                }
            }
            dialog.dismiss();
        }
    }

    /**
     * 下载完成,提示用户安装
     */
    private void installApk(File file) {
        //调用系统安装程序
        Intent intent = new Intent();
        intent.setAction("android.intent.action.VIEW");
        intent.addCategory("android.intent.category.DEFAULT");
        intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
        intent.setDataAndType(Uri.fromFile(file), "application/vnd.android.package-archive");
        //启动activity -第二个参数是请求码，随便设置，但是必须大于0
        startActivityForResult(intent, REQUEST_INSTALL_CODE);
    }

    /**
     * 跳转到登录界面
     */
    private void load2Login() {
        new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    Thread.sleep(2000);
                    Intent toLogin = new Intent(MainActivity.this, LoginActivity.class);
                    startActivity(toLogin);
                    finish();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }).start();
         Log.d("hah","测试成功");
    }

    /**
     * 跳转到主界面
     */
    private void load2MainActivity() {
        Intent toMainActivity = new Intent(MainActivity.this, MainActivity.class);
        startActivity(toMainActivity);
        finish();
    }

    /**
     * 获取设备序列号
     */
    private String getSerialNumber() {
        String serial = null;
        try {
            Class<?> c = Class.forName("android.os.SystemProperties");
            Method get = c.getMethod("get", String.class);
            serial = (String) get.invoke(c, "ro.serialno");
        } catch (Exception e) {
            e.printStackTrace();
        }
        return serial;
    }

    /**
     * 封装版本升级数据
     */
    private class VersionDatas {
        String COMMAND = "GET_APP_VERSION";
        String DEVICE_NAME = deviceName;
        String DEVICE_SN = serialNumber;
    }
}


