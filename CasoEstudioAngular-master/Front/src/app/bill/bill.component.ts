import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { ClientService } from '../client.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-bill',
  templateUrl: './bill.component.html',
  styleUrls: ['./bill.component.css'],
})
export class BillComponent implements OnInit {
  form: FormGroup;
  // tslint:disable-next-line: variable-name
  img_background = './assets/background.jpg';
  // tslint:disable-next-line: variable-name
  img_circle = './assets/register-fac.png';
  facturas: [];
  idbill: string;
  customerID: string;
  customerName: string;
  customerLastname: string;
  customerLine : string;
  // tslint:disable-next-line: variable-name

  constructor(
    private fb: FormBuilder,
    private client: ClientService,
    private route: Router
  ) {}
  ngOnInit(): void {
    this.form = this.fb.group({
      mobileline: ['', Validators.required],
      date: ['', Validators.required],
    });
  }

  // tslint:disable-next-line: typedef
  async onSubmit() {
    if (this.form.valid) {
      this.client
        .getRequest(
          `http://localhost:5000/api/v01/bill/get/${this.form.value.mobileline}`,
          localStorage.getItem('token')
        )
        .subscribe((Response: any) => {
          console.log(Response);
          const { facturas } = Response;
          console.log(this.form.value.date);
          // tslint:disable-next-line: typedef
          const { idcustomer, name, lastname, line } = Response;
          this.facturas = facturas;
          this.customerID = idcustomer;
          this.customerName = name;
          this.customerLastname = lastname;
          this.customerLine = line;
          this.form.reset();
        }),
        // tslint:disable-next-line: no-unused-expression
        (error) => {
          console.log(error.status);
        };
    } else {
      console.log('error en el ingreso de datos');
    }
  }
  // tslint:disable-next-line: typedef
  async onSubmit2(item: any) {
    if (this.form.valid) {
      this.client
        .deleteRequest(
          `http://localhost:5000/api/v01/bill/delete/${item}`,
          localStorage.getItem('token')
        )
        .subscribe((Response: any) => {
          console.log(Response);
        }),
        // tslint:disable-next-line: no-unused-expression
        (error) => {
          console.log(error.status);
        };
    } else {
      console.log('error en el ingreso de datos');
    }
  }
}
