//
//  HowOldAppDelegate.h
//  HowOld
//
//  Created by Swizec on 1/9/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>

@class HowOldViewController;

@interface HowOldAppDelegate : NSObject <UIApplicationDelegate> {
    UIWindow *window;
    HowOldViewController *viewController;
}

@property (nonatomic, retain) IBOutlet UIWindow *window;
@property (nonatomic, retain) IBOutlet HowOldViewController *viewController;

@end

