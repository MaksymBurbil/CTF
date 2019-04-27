import java.math.BigInteger;
import java.security.MessageDigest;

class g {
    private static byte[] a = new byte[]{(byte) 48, (byte) 59, (byte) 44, (byte) 59, (byte) 116, (byte) 41, (byte) 63, (byte) 57, (byte) 47, (byte) 40, (byte) 51, (byte) 46, (byte) 35, (byte) 116, (byte) 23, (byte) 63, (byte) 41, (byte) 41, (byte) 59, (byte) 61, (byte) 63, (byte) 30, (byte) 51, (byte) 61, (byte) 63, (byte) 41, (byte) 46};
    private static byte[] b = new byte[]{(byte) -30, (byte) -32, (byte) -15, (byte) -52, (byte) -21, (byte) -10, (byte) -15, (byte) -28, (byte) -21, (byte) -26, (byte) -32};
    private static byte[] c = new byte[]{(byte) 65, (byte) 72, (byte) 57};
    private static String d = new String(a);
    private static String e = new String(b);
    private static String f = new String(c);

    static {
        int i;
        byte[] bArr;
        String test;
        int i2 = 0;
        for (i = 0; i < a.length; i++) {
            bArr = a;
            bArr[i] = (byte) (bArr[i] ^ 90);
      
        }
        
        for (i = 0; i < b.length; i++) {
            bArr = b;
            bArr[i] = (byte) (bArr[i] ^ -123);
        }
        while (i2 < c.length) {
            byte[] bArr2 = c;
            bArr2[i2] = (byte) (bArr2[i2] ^ 12);
            i2++;
        }
    }

    public static byte[] a(byte[] bArr) {
        try {
            MessageDigest messageDigest;
            messageDigest = MessageDigest.getInstance("MD5");
            messageDigest.update(bArr);
            return messageDigest.digest();
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}

public class Android1 {
    public static void main(String args[]) {


        byte[] b = new byte[16];


        byte[] bArr = new byte[]{(byte) 100, (byte) -1, Byte.MAX_VALUE, (byte) -57, (byte) -59, (byte) 62, (byte) 56, (byte) 8, (byte) 46, (byte) -40, (byte) -52, (byte) -10, (byte) -104, (byte) -74, (byte) 12, (byte) -63};

        byte[] b1;

        BigInteger bb1 = new BigInteger("338062061179655452874859029801038120598");
        b1 = bb1.toByteArray();

        for(int i = 0; i < 16; i++)
            b[i] = (byte)b1[i+1];
                
        for(int i = 0; i < 16; i++)
            b[i] = (byte)(b[i] + bArr[i]);
            
        BigInteger bd1 = new BigInteger(1, b);
        
        System.out.println(bd1.toString(16));
    

    }
}