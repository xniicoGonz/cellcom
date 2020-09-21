import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { ClientService } from '../client.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-bill',
  templateUrl: './bill.component.html',
  styleUrls: ['./bill.component.css']
})
export class BillComponent implements OnInit {
  form: FormGroup;
  // tslint:disable-next-line: variable-name
  img_background = './assets/background.jpg';
  // tslint:disable-next-line: variable-name
  img_circle = './assets/register-fac.png';
  identificationCard: string;
  lastname: string;
  line: string;
  name: string;
  datebill: string;
  // tslint:disable-next-line: variable-name
  id_fac: string;
  valuefac: string;

  constructor(
    private fb: FormBuilder,
    private client: ClientService,
    private route: Router
    ){}
  ngOnInit(): void {
  this.form = this.fb.group({
    mobileline: ['', Validators.required],
    date: ['', Validators.required]
  });
  }

 // tslint:disable-next-line: typedef
 async onSubmit(){
   if (this.form.valid){
     this.client
       .getRequest(
         `http://localhost:5000/api/v01/bill/get/${this.form.value.mobileline}`,
         localStorage.getItem('token')
       )
       .subscribe((Response: any) => {
         // console.log(Response);
         const {  name, lastname, identification, line} = Response;
         const { value, id_bill, collectionDay } = Response;
         this.identificationCard = identification;
         this.name = name;
         this.lastname = lastname;
         this.line = line;
         this.valuefac = value;
         this.id_fac = id_bill;
         this.datebill = collectionDay;
        }),
       // tslint:disable-next-line: no-unused-expression
       (error) => {
         console.log(error.status);
       };
   }else{
     console.log('error en el ingreso de datos');
   }
 }
// tslint:disable-next-line: typedef
async onSubmit2(){
   if (this.form.valid){
     this.client
       .deleteRequest(
         `http://localhost:5000/api/v01/bill/delete/${this.form.value.mobileline}`,
         localStorage.getItem('token')
       )
       .subscribe((Response: any) => {
         // console.log(Response);
         const {usuario} = Response;
        }),
       // tslint:disable-next-line: no-unused-expression
       (error) => {
         console.log(error.status);
       };
   }else{
     console.log('error en el ingreso de datos');
   }
 }
}
