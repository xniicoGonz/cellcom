import { Component, OnInit } from '@angular/core';
import { ClientService } from '../client.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-line',
  templateUrl: './line.component.html',
  styleUrls: ['./line.component.css'],
})
export class LineComponent implements OnInit {
  form: FormGroup;
  form2: FormGroup;
  // Inyeccion de dependencias
  constructor(
    private fb2: FormBuilder,
    private fb: FormBuilder,
    private client: ClientService,
    private route: Router
  ) {}

  // tslint:disable-next-line: variable-name
  img_background = './assets/background.jpg';
  // tslint:disable-next-line: variable-name
  img_circle = './assets/register-line.png';
  customerID: string;
  customerLine: string = '';
  customerState: string;
  customerTrademark: string;
  ngOnInit(): void {
    this.form = this.fb.group({
      mobileLine: ['', Validators.required],
    });
    this.form2 = this.fb2.group({
      line2: ['', Validators.required],
      personID: ['', Validators.required],
      state: ['', Validators.required],
      tradeMark: ['', Validators.required],
    });
  }


  // tslint:disable-next-line: typedef
  async onSubmit() {
    if (this.form.valid) {
      this.client.getRequest(
          `http://localhost:5000/api/v01/line/get/${this.form.value.mobileLine}`,
          localStorage.getItem('token')
        )
        .subscribe((response: any) => {
          // el objeto json que recibe tiene las propiedades 'linea' y 'Status, usuario'
          const { Status } = response;
          const { linea, id, state, trademark } = response;
          this.customerID = id;
          this.customerLine = linea;
          this.customerState = state;
          this.customerTrademark = trademark;
          console.log(Status);
          // tslint:disable-next-line: no-unused-expression
          console.log(this.form2.value);
          console.log(this.form.status);
          console.log(this.form2.status);
          this.form.reset();
        }),
        // tslint:disable-next-line: no-unused-expression
        (error) => {
          console.log(error.status);
        };
    } else {
      console.log('Error en el ingreso de datos');
      console.log(this.form2.value.line2);
      console.log(this.form2.value.personID);
      console.log(this.form2.value.state);
      console.log(this.form2.value.tradeMark);
      


    }
  }
  // tslint:disable-next-line: typedef
  // tslint:disable-next-line: typedef
  async onSubmit2() {
    if (this.form2.valid) {
      this.client
        .putRequest(
          `http://localhost:5000/api/v01/line/put/${this.form2.value.personID}`,
          {
            line2: this.form2.value.line2,
            personID: this.form2.value.personID,
            state: this.form2.value.state,
            tradeMark: this.form2.value.tradeMark,
          },
          localStorage.getItem('token')
        )
        .subscribe((response: any) => {
          // el objeto json que recibe tiene las propiedades 'linea' y 'Status, usuario'
          console.log(response);
          console.log('por el onsubimte2');
          console.log( this.form2.value.line2,
             this.form2.value.personID,
             this.form2.value.state,
             this.form2.value.tradeMark);
          this.form2.reset();

        }),
        // tslint:disable-next-line: no-unused-expression
        (error) => {
          console.log(error.status);
        };
    } else {
      console.log('Error en el ingreso de datos');
      console.log(
              this.form2.value.line2,
              this.form2.value.personID,
              this.form2.value.state,
              this.form2.value.tradeMark
            );
    }
  }
  // tslint:disable-next-line: typedef
  async onSubmit3() {
    if (this.form2.valid) {
      this.client
        .postRequest(
          `http://localhost:5000/api/v01/line/register`,
          {
            line2: this.form2.value.line2,
            personID: this.form2.value.personID,
            state: this.form2.value.state,
            tradeMark: this.form2.value.tradeMark,
          },
          localStorage.getItem('token')
        )
        .subscribe((response: any) => {
          // el objeto json que recibe tiene las propiedades 'linea' y 'Status, usuario'
          console.log(response);
          console.log(' por el onsubimit 3 ');
          this.form2.reset();
        }),
        // tslint:disable-next-line: no-unused-expression
        (error) => {
          console.log(error.status);
        };
    } else {
      console.log('Error en el ingreso de datos');
    }
  }
}
