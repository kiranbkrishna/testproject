import math.{max}

object LCS {
    def lcs(s1:String, s2:String) : Int = {
            val m = s1.length()
            val n = s2.length()
            var c = Array.tabulate(m,n){(m,n)=> 0 }
            for (i <- 1 to m-1; j <- 1 to n-1){
                if (s1.charAt(i) == s2.charAt(j))
                    c(i)(j) = c(i-1)(j-1) + 1
                else
                    c(i)(j) = max(c(i)(j-1), c(i-1)(j))
            } 
            println ("" + c(m-1)(n-1))
            return c(m-1)(n-1)
    }

   def main(args: Array[String]): Unit = {
      lcs("rosettacode", "raisethysword")
   }
 }
