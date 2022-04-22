class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Method to set the default state of the TV.
        """
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__status = False


    def power(self):
        """
        Method to turn the TV off.
        """
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False


    def channel_up(self):
        """
        Method to turn the volume up
        """
        if self.__status == True:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL


    def channel_down(self):
        """
        Method to change channel down.
        """
        if self.__status == True:
            if self.__channel < Television.MAX_CHANNEL:
                self.__chanel -= 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def volume_up(self):
        """
        - This method should be used to adjust the TV volume by incrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_VOLUME, the volume should not be adjusted.
        """
        if self.__status == True:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            else:
                self.__volume = Television.MAX_VOLUME

    def volume_down(self):
        """
        - This method should be used to adjust the TV volume by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_VOLUME, the volume should not be adjusted.

        """
        if self.__status == True:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            else:
                self.__volume = Television.MIN_VOLUME

    def __str__(self):
        """
        - This method should be used to return the TV status using the format shown in the comments of main.py
        """
        return f'TV Status: Is On = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
