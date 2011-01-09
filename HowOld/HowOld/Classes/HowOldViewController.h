//
//  HowOldViewController.h
//  HowOld
//
//  Created by Swizec on 1/9/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface HowOldViewController : UIViewController 
<UIPickerViewDataSource , UIPickerViewDelegate, UITextFieldDelegate>
{
  IBOutlet UIPickerView *yearPicker;
  IBOutlet UITextField *celebrity;
  IBOutlet UIProgressView *fetchProgress;
  NSArray *pickerData;
}

@property(nonatomic , retain) UIPickerView *yearPicker;
@property(nonatomic , retain) UITextField *celebrity;
@property(nonatomic , retain) UIProgressView *fetchProgress;
@property(nonatomic , retain) NSArray *pickerData;
@property(nonatomic) int currentYear;

-(IBAction) textFieldDoneEditing : (id) sender;
-(IBAction) backgroundTap:(id) sender;

-(IBAction)buttonPressed;
-(int)getCurrentYear;

@end