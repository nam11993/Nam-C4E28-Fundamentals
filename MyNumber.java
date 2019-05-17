package testmaster;

public class MyNumber {
    public int TinhGiaiThua(int number)
    {
        int kq=1;
        for(int i=1; i<number; i++)
        {
            kq = kq*i;
        }
        return kq;
    }

    public boolean KiemTraSoNguyenTo(int number)
    {
        boolean kq=true;
        for(int i=2; i<number; i++)
        {
            if(number%i==0)
            {
                kq=false;
                break;
            }
        }
        return kq;

    }
}
