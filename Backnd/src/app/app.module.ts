import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import { EmployeeFormComponent } from './employee-form/employee-form.component';
import { AppRoutingModule } from './app-routing.module';
import { MaterialModule } from './material.module';
@NgModule({
  declarations: [
    AppComponent,
    EmployeeFormComponent
    // Other components
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule
    // Other modules
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }