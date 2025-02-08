import SwiftUI
import CoreLocation

struct ContentView: View {
    @ObservedObject var compass = Compass()
    
    var body: some View {
        VStack {
            Text("Heading: \(compass.heading, specifier: "%.2f")°")
                .font(.largeTitle)
                .padding()
            Image(systemName: "location.north.fill")
                .resizable()
                .aspectRatio(contentMode: .fit)
                .frame(width: 200, height: 200)
                .rotationEffect(.degrees(compass.heading))
                .animation(.easeInOut)
        }
        .onAppear {
            compass.start()
        }
        .onDisappear {
            compass.stop()
        }
    }
}

class Compass: NSObject, ObservableObject, CLLocationManagerDelegate {
    private var locationManager: CLLocationManager
    @Published var heading: Double = 0.0
    
    override init() {
        locationManager = CLLocationManager()
        super.init()
        locationManager.delegate = self
        locationManager.headingFilter = 1
        locationManager.requestWhenInUseAuthorization()
    }
    
    func start() {
        if CLLocationManager.headingAvailable() {
            locationManager.startUpdatingHeading()
        }
    }
    
    func stop() {
        locationManager.stopUpdatingHeading()
    }
    
    func locationManager(_ manager: CLLocationManager, didUpdateHeading newHeading: CLHeading) {
        heading = newHeading.magneticHeading
    }
}

@main
struct CompassApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
