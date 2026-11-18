import re
m='android/app/src/main/AndroidManifest.xml'
s=open(m).read()
perms=['BLUETOOTH','BLUETOOTH_ADMIN','BLUETOOTH_CONNECT','BLUETOOTH_SCAN','ACCESS_FINE_LOCATION']
add=''.join('    <uses-permission android:name="android.permission.%s" />\n'%p for p in perms if 'android.permission.%s"'%p not in s)
s=s.replace('<application',add+'    <application',1)
open(m,'w').write(s)
v='android/variables.gradle'
t=open(v).read()
t=re.sub(r'targetSdkVersion\s*=\s*\d+','targetSdkVersion = 30',t)
open(v,'w').write(t)
print('patched')
