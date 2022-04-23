// Can be run on https://dotnetfiddle.net

using System;
using System.Text;
using System.Web;

public class Program
{	
	public static String encoding(String plain){
		// null Char
		Char NULL = char.MinValue;
		String extended_plain = "";
		for (int i=0; i<plain.Length; i++){
			extended_plain += plain[i];
			extended_plain += NULL;
		}
		String cipher = HttpServerUtility.UrlTokenEncode(Encoding.UTF8.GetBytes(extended_plain));
		return cipher;
	}
	
	public static void Main()
	{	
		// Input information
		// -- Not important (can be ignored)
		String dateLst     = "2022/5/31";    // Last date of the month, no padding, ex:2022/4/30
		String buildingSeq = encoding("0");  // Not sure what it is
		String section     = encoding("2");  // Ex:8:00~9:00=1, 9:00~10:00=2
		String week        = encoding("5");  // Week of the month
		// -- Important (need to be modified everytime)
		String date        = encoding("2022/05/20");
		String placeSeq    = encoding("1");  // Floor : {1=3F} | {2=1F}
		String sTime       = encoding("16"); // Starting time
		String eTime       = encoding("18"); // Ending time
		
		// Get full url
		String url = "https://ntupesc.ntu.edu.tw/facilities/PlaceOrderFrm.aspx?";
		url += String.Format("buildingSeq={0}&placeSeq={1}&dateLst={2}&", buildingSeq, placeSeq, dateLst);
		url += String.Format("sTime={0}&eTime={1}&section={2}&", sTime, eTime, section);
		url += String.Format("date={0}&week={1}", date, week);
		Console.WriteLine(url);
		
		// Decode
		var cipher = "MwA1";
		var cipherTokenDecode = Encoding.UTF8.GetString(HttpServerUtility.UrlTokenDecode(cipher));
		var cipherTokenEncode = HttpServerUtility.UrlTokenEncode(Encoding.UTF8.GetBytes(cipherTokenDecode));
		Console.WriteLine(String.Format("\nDecoding\n\tCipher : {0} ---> Plain : {1}", cipherTokenEncode, cipherTokenDecode));
	}
}