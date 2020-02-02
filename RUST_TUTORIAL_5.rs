fn main(){
    let a=123;
    {
        #shadowing
        let a=5;
        let b=321;
        println!("{} {}",a,b);
    }
    println!("{}",a);


}
