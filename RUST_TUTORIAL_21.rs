
//passing the ownership

fn main(){
    let a =String::from("total technology");
    let b =func_strin(a);
    println!("{}",b);
    }
    fn func_strin(s:String)->String{
    s
    }


//without passing the ownership only rerefence
fn main(){

    let a =String::from("total technology");
    func_strin(&a);//not passing ownership only refering to variable 
    println!("actual string is {}",a); //no error

}

fn func_strin(s:&String){
    println!("{}",s);

}



   