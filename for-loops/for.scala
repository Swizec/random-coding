
object forVarReuse extends App {
       var i=5;

       for (i<-1 to 2) {
           println("for:"+i);
       }

       println("after:"+i);
}
