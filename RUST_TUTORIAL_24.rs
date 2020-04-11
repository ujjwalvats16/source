

//GENERAL APPROACH

fn main(){
    struct emp{
    name:String,
    company:String,
    city:String,
    }
    let EMP=emp{
    name:String::from("RONI"),
    company:String::from("abc"),
    city:String::from("mumbai"),
    };
    let EMP1=emp{
    name:String::from("JOHN"),
    company:EMP.company,
    city:EMP.city,
    };
    println!("{} {} {}",EMP1.name,EMP1.company,EMP1.city);
    }

//BEST APPROACH

fn main(){
    struct emp{
    name:String,
    company:String,
    city:String,
    }
    let EMP=emp{
    name:String::from("RONI"),
    company:String::from("abc"),
    city:String::from("mumbai"),
    };
    let EMP1=emp{
    name:String::from("JOHN"),
    ..EMP
    };
    println!("{} {} {}",EMP1.name,EMP1.company,EMP1.city);
    }
    