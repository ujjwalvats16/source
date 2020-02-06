fn main(){

    //tuple

    let a=(1,2,3,4);
    println!("{} {} {} {}",a.0,a.1,a.2,a.3);

    let a:(i32,i32,i32,i32)=(1,2,3,4);
    println!("{} {} {} {}",a.0,a.1,a.2,a.3);

    //array

    let a=[1,2,3];
    println!("{} {} {}",a[0],a[1],a[2]);

    let a:[i32;4]=[1,2,3,4];
    println!("{} {} {}",a[0],a[1],a[2]);


    // sample exercise

    let a=(1,2,3);
    let (x,y,z)=a;
    println!("{} {} {}",x,y,z);



}