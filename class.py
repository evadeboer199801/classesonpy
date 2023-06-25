class DetachPatrol_adeptus_ministorum(DetachPatrol):
    army_name = u'Adeptus Ministorum (Patrol detachment)'
    faction_base = u'ADEPTUS MINISTORUM'
    alternate_factions = []
    army_id = u'patrol_adeptus_ministorum'
    army_factions = [u'IMPERIUM', u'ADEPTA SORORITAS', u'<ORDER>', u'ADEPTUS MINISTORUM']

    def __init__(self, parent=None):
        super(DetachPatrol_adeptus_ministorum, self).__init__(*[], **{u'heavy': True, u'troops': True, u'transports': True, u'hq': True, u'fast': True, u'elite': True, u'parent': parent, })
        self.heavy.add_classes([Exorcist, Retributors, PenitentEngines])
        self.troops.add_classes([BattleSisters])
        self.transports.add_classes([ASRhino, Immolator])
        self.hq.add_classes([Celestine, Canoness, Jacobus])
        self.fast.add_classes([Dominions, Seraphims])
        self.elite.add_classes([ArcoFlagellants, Assassins, Celestians, Dialogus, Hospitaller, Imagifier, Mistress, Priest, Repentia, PriestV2, Crusaders])
        return None
