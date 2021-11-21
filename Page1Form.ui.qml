import QtQuick 2.11
import QtQuick.Controls 2.4

Page {
    id: page
    width: 600
    height: 400

    property alias icon: icon

    property alias bottomLeftRect: bottomLeftRect
    property alias middleRightRect: middleRightRect
    property alias topLeftRect: topLeftRect

    property alias mouseArea2: mouseArea2
    property alias mouseArea1: mouseArea1
    property alias mouseArea: mouseArea

    font.pixelSize: 8

    header: Label {
        text: qsTr("Page 1")
        font.pixelSize: Qt.application.font.pixelSize * 2
        padding: 10
    }

    Image {
        id: icon
        x: 10
        y: 20
        fillMode: Image.PreserveAspectFit
        source: "qt-logo.png"
    }

    Rectangle {
        id: topLeftRect
        width: 55
        height: 41
        color: "#00000000"
        anchors.top: parent.top
        anchors.topMargin: 20
        anchors.left: parent.left
        anchors.leftMargin: 10
        border.color: "#808080"

        MouseArea {
            id: mouseArea
            anchors.fill: parent
        }
    }

    Rectangle {
        id: middleRightRect
        width: 55
        height: 41
        color: "#00000000"
        anchors.right: parent.right
        anchors.rightMargin: 10
        anchors.verticalCenter: parent.verticalCenter
        border.color: "#808080"

        MouseArea {
            id: mouseArea1
            anchors.fill: parent
        }
    }

    Rectangle {
        id: bottomLeftRect
        width: 55
        height: 41
        color: "#00000000"
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 20
        anchors.left: parent.left
        anchors.leftMargin: 10
        border.color: "#808080"

        MouseArea {
            id: mouseArea2
            anchors.fill: parent
        }
    }
}




/*##^## Designer {
    D{i:4;anchors_height:100;anchors_width:100;anchors_x:8;anchors_y:8}D{i:3;anchors_x:10;anchors_y:20}
D{i:6;anchors_height:100;anchors_width:100;anchors_x:16;anchors_y:18}D{i:5;anchors_height:41;anchors_width:55;anchors_x:10;anchors_y:20}
D{i:8;anchors_height:100;anchors_width:100;anchors_x:26;anchors_y:19}D{i:7;anchors_height:41;anchors_x:10;anchors_y:20}
}
 ##^##*/
