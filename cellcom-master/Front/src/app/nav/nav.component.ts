import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent implements OnInit {
  constructor(private route: Router) { }


  // tslint:disable-next-line: member-ordering
  token = '';
  userInSystem  = false;
  // tslint:disable-next-line: typedef
  welcome(){
    this.route.navigate(['']);
  }

  // tslint:disable-next-line: typedef
  login(){
    this.route.navigate(['login']);
  }


  // tslint:disable-next-line: typedef
  registerConsultant(){
    this.route.navigate(['/registerConsultant']);
  }

  // tslint:disable-next-line: typedef
  registerCustomer(){
    this.route.navigate(['/registerCustomer']);
  }

  // tslint:disable-next-line: typedef
  registerEquipment(){
    this.route.navigate(['/registerEquipment']);
  }

  // tslint:disable-next-line: typedef
  line(){
    this.route.navigate(['/line']);
  }

  // tslint:disable-next-line: typedef
  consultantBill(){
    this.route.navigate(['/consultantBill']);
  }

  ngOnInit(): void {
    this.token = localStorage.getItem('token');
    if (this.token){
      this.userInSystem = true;
    }else{
      this.userInSystem = false;
    }
  }
  // tslint:disable-next-line: typedef
  closeSesion(){
  localStorage.removeItem('token');
  }
}
