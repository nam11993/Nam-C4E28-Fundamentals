//Phan 1:
package testmaster;

//Phan 2:

import static org.junit.Assert.assertTrue;

import org.junit.*;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

/**
 * Unit test for simple App.
 */
//Phan 3:
public class AppTest {
    /**
     * Rigorous Test :-)
     */

    /*
        @Test là một Annotation (Chỉ dẫn cho Framewrork hoạt động)
        @Test chỉ ra phần code ở bên dưới nó là một TestMethod (Testcase)

        @Before - Là một Annotation đánh dấu code ở bên dưới sẽ đc chạy
        trước mỗi testmethod (Testcase)

        @After - Là một Annotation đánh dấu code sẽ sau một Testmethod
     */
    @Test
    public void Test_KTSoNguyenTo_KoPhaiSNT() {
        //Given - Cài đặt các giả thiết trong Testcase
        int number = 4;
        boolean ExpectedKQ = false;
        boolean KQ = true;

        //When - Thực hiện các hành động trong Testcase
        MyNumber myNumber = new MyNumber();
        KQ = myNumber.KiemTraSoNguyenTo(number);

        //Then - Thực hiện các kiểm tra để ghi nhận kết quả Test
        Assert.assertEquals(ExpectedKQ, KQ);
    }

    @Test
    public void Test_KTSoNguyenTo_DungLaSNT()
    {
        //Given
        int number=5;
        boolean expectedResult = true;
        boolean actualResult = false;

        //When
        MyNumber myNumber = new MyNumber();
        actualResult = myNumber.KiemTraSoNguyenTo(number);

        //Then
        Assert.assertEquals(expectedResult, actualResult);
    }

    @Test
    @Ignore
    public void SecondTestCase() {

    }

}
