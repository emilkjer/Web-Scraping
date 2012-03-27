/******************************************************
 * RMIT University, Melbourne
 * Date 27 Mar 2012
 * By Emil Broegger Kjer
 * For questions or comments contact emil@kjer.info
 ******************************************************/


//Remember to set the jsoup library class
//export CLASSPATH=/Users/emil/study/rmit/semester4/scraping_talk/code/example_java/lib/jsoup-1.6.1.jar:$CLASSPATH

/* JSOUP REFERENCES
 * project location http://jsoup.org/
 * library http://jsoup.org/packages/jsoup-1.6.1.jar
 * API location: http://jsoup.org/apidocs/
 * extracting elements: http://jsoup.org/cookbook/extracting-data/attributes-text-html
 * load from file: http://jsoup.org/cookbook/input/load-document-from-file
 */

import java.io.*;
import org.jsoup.*;
import org.jsoup.nodes.*;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;


public class ScrapeSimple
{
    public static void main(String args [])
    {
        try
            {
                // From URL
                //Train Epping Line
                // String url = "http://tt.metlinkmelbourne.com.au/tt/XSLT_TTB_REQUEST?command=direct&language=en&outputFormat=0&net=vic&line=02EPP&project=ttb&itdLPxx_selLineDir=R&sup=B";
                
                //Bus
                // String url = "http://tt.metlinkmelbourne.com.au/tt/XSLT_TTB_REQUEST?command=direct&language=en&net=vic&line=04C01&sup=A&project=ttb&outputFormat=0&itdLPxx_loadNTPs=1&itdLPxx_showNTPS=2&itdLPxx_selLineDir=H&itdLPxx_selWDType=T0&itdLPxx_scrollOffset=1735";
                

                // Create the document to parse
                // Remark: To avoid a timeout on the connection set the timeout relatively high
                Document doc = Jsoup.connect(url).timeout(10*1000).get();
                
                


                // From file
                // File input = new File("./data/timetables/epping_line_weekday_true.html");
                // Document doc = Jsoup.parse(input, "UTF-8", "");
                
                
                
                Elements divs_stops = doc.select("div.ma_stop");	
                for (Element el : divs_stops){
                    System.out.println(el.text());
                }
                
                Elements divs_times = doc.select("div#ttBR_row_1");	
                for (Element el : divs_times){
                    System.out.println(el.text());
                }
                
                // Maybe this could be a help?
                // Elements divs_all_times = doc.select("div.ttBodyTP");	
                // for (Element el : divs_all_times){
                //     System.out.println(el.text());
                // }
                
            }
        catch (IOException e)
            {
                e.printStackTrace();
            }
    }
    
}
