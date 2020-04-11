fn main(){

    //define the strucy
    struct emp{
        name:String,
        company:String,
        i_d:u64,

    }
    //creating an instance of the prefedined struct
    let Emp=emp{
        name:String::from("roni"),
        i_d:1,
        company:String::from("totaltechnology"),

    };
     //accesing struct elements using name
    println!("{}",Emp.company);
    println!("{}",Emp.name);
    println!("{}",Emp.i_d);


}

