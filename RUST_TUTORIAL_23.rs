fn main(){

    struct emp{
       name:String,
       company:String,
    
    }
    
    let mut EMP=emp{
        name:String::from("roni"),
        company:String::from("abc"),
    };
    
    EMP.company=String::from("xyz");
    println!("{}",EMP.company);
    
    }